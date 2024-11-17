
#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include <unistd.h>
#include <stddef.h>
#include <math.h>
#include <error.h>
#include <stdlib.h>
#include <errno.h>

#define MSTR(s) #s
#define STR(s) MSTR(s)
#define SZ 120
#define CHKPTR(ptr) if (ptr == NULL) { error(errno, errno, __FILE__ ":" STR(__LINE__)); }

#ifndef EPSILON
#define EPSILON 0.1
#endif

#define MAX(a, b) a > b ? a : b
#define MIN(a, b) a < b ? a : b



struct point {
        double x;
        double y;
};


struct gate {
      struct point point[2];
};


long unsigned n = 0;
long unsigned r = 0;



static inline double slope(struct point a, struct point b)
{
        return ((double) (a.y - b.y)) / ((double) (a.x - b.x));
}

static inline double elevation(struct point a, double slope) 
{
        return (double) a.y - slope * (double) a.x;
}

/* Funktion prepare_gate:
 * 	Verändert die x-Koordinate so, dass der Ball durch das Tor hindurchpasst.
 * 	Parameter: 
 * 		struct gate *gate			Das zu verändende Tor
 * 	Rückgabewert:
 * 		int					Erfolg
 * 
 *
 */


char prepare_gate(struct gate *gate) 
{
	
	// Falls ein Tor komplett senkrecht steht. 
	if (gate->point[0].x == gate->point[1].x) {
		gate->point[0].y -= r;
		gate->point[1].y += r;
		return 1;
	}

	double x = fabs(gate->point[0].x - gate->point[1].x);
	double y = fabs(gate->point[0].y - gate->point[1].y);
	if (sqrt(x * x + y * y) < 2 * r) {
		printf("Es gibt mindestens ein Tor, durch welches der Ball nicht hindurchpasst.\n");
		return 0;
	}
	double g = (r * x) / sqrt(x * x + y * y); 
	if (gate->point[0].x > gate->point[1].x) {
		gate->point[0].x -= g;
		gate->point[1].x += g;
	} else {
		gate->point[1].x -= g;
		gate->point[0].x += g;
	}
	return 1;
}


/*  Funktion open_file:
 *  	Öffnet gegebene Datei und liest die Informationen aus der Datei in eine Liste aus.
 *  	Parameter:
 *  		char *path				Pfad der Datei mit den Informationen
 *  	Rückgabewert:
 *  		struct gate*				List der Tore. Die Länge wird durch die globale Variable n beschrieben.
 *
 *
 */

struct gate* open_file(char *path)
{
	FILE *fp = fopen(path, "r");
	CHKPTR(fp);

	char str[SZ];


	if (fgets(str, sizeof(str), fp) != NULL) {
		sscanf(str, "%lu %lu", &n, &r);
	} else { 
		error(errno, errno, __FILE__ ":" STR(__LINE__));
	}


	struct gate *gate = malloc((n + 1) * sizeof(struct gate));
	if (gate == NULL) {
		error(errno, errno, __FILE__ ":" STR(__LINE__));
	} 

	uint64_t i = 0;
	while(fgets(str, SZ, fp) != NULL && i < n) {
		sscanf(str, "%lf %lf %lf %lf", &(gate[i].point[0].x), &(gate[i].point[0].y), &(gate[i].point[1].x), &(gate[i].point[1].y)); 
		if (!prepare_gate(&gate[i])) {
			free(gate);
			return NULL;
		}
		i++;
	}

	if (ferror(fp)) {
		error(errno, errno, __FILE__ ":" STR(__LINE__));
	}


	fclose(fp);
	return gate;
}

/*  Funktion solve:
 *
 *  Parameter: 	
 *  	struct point start			der Punkt, für welchen ausgerechnet wird, ob von ihm aus ein Ziel erreicht werden kann.
 *  	const struct gate *gates 			ein Feld, welches die Koordinaten der Anfangs- und Endpunkte der jeweiligen Ziele enthält. Es muss mindestens ein Eintrag am Pointer enthalten sein.
 *  
 *
 *  	size_t  n				anzahl Elemente in dem Feld ,,gates''
 *  Rückgabewert: 
 *  	Falls erfolgreich: Winkel der Gerade, welche das Ziel erreicht (Mittelwert des größtmöglichen und kleinstmöglichen Winkels) 
 *  	Falls nicht erfolgreich / oder n < 2: -1
 *
 */

double solve(struct point start, const struct gate *gates, size_t n) 
{
	
	double angles[2];
	for (int j = 0; j < 2; j++) {
		angles[j] = atan2(gates[1].point[j].y - start.y, gates[1].point[j].x - start.x);
	}
	double lower = MIN(angles[0], angles[1]);
	double upper = MAX(angles[0], angles[1]);



	for (size_t i = 2; i < n; i++) {
		for (int j = 0; j < 2; j++) {
			angles[j] = atan2(gates[i].point[j].y - start.y, gates[i].point[j].x - start.x);
		}


		double clower = MIN(angles[0], angles[1]);
		double cupper = MAX(angles[0], angles[1]);



		if (clower > upper) {
			return -5;
		} 

		if (cupper < lower) {
			return -5;
		}

		if (clower < lower) {
			clower = lower;
		} 


		if (upper < cupper) {
			cupper = upper;
		}

		upper = cupper;
		lower = clower;
	}
	// Der Winkel der in der Mitte liegt. 
	
	return  (lower + upper) / 2;

}







int main(int argc, char **argv) 
{
	if (argc < 2) {
		fprintf(stderr, "Verwendung: fünf [Pfad zur Datei]\n");
		return 1;
	}

	struct gate *gates = open_file(argv[1]);
	if (gates == NULL) {
		return 2;
	} 
	if (n < 1) {
		free(gates);
		return 0;
	} 
	double cx = MIN(gates[0].point[0].x, gates[0].point[1].x); 
	double mx = MAX(gates[0].point[0].x, gates[0].point[1].x); 

	double cy = MAX(gates[0].point[0].y, gates[0].point[1].y); 
	double my = MIN(gates[0].point[0].y, gates[0].point[1].y); 

	double m = slope(gates[0].point[0], gates[0].point[1]);
	double t = elevation(gates[0].point[0], m); 

	double plus = EPSILON / (sqrt(1 + m * m));

	char loop = 1;

	while(loop) {
		struct point point;
		if (cx == mx) {
			loop = cy > my ? 1 : 0; 
			point = (struct point) {cx, cy};
			cy -= EPSILON;
		} else {
			loop = cx < mx ? 1 : 0; 
			point = (struct point) {cx, cx * m + t};
			cx += plus;
		}
		double solution = 0;
		if ((solution = solve(point, gates, n )) > -  M_PI)  {
			printf("(x: %lf | y: %lf), Winkel: %lf Grad\n ", point.x, point.y, solution *57.2958); 
			break;
		}
	}

	free(gates);


	return 0;
}
