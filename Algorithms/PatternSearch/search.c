/* FILE NAME: kmp.c 
   FILE PATH: /Users/chuan/Github/COMP10002/kmp.c	 
   USER NAME:  Chuanyuan Liu */
   
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <ctype.h>
#include <limits.h>
#include <string.h>
#include <assert.h>
#include <time.h>

void buildkmp(const char *p, int *f, const int m){
	int s = 2, c = 0, i;
	f[0] = -1; 
	f[1] = 0;
	while (s < m) {
		/* match */
		if (p[c] == p[s-1]) {
			f[s] = c + 1;
			c++;
		} /* no match */
		else if (c > 0) {
			c = f[c];
			f[s] = 0;
		} 
		else {
			f[s] = 0;
		}
		s++;
	} 
	for (i = 0; i < m; i++){
		printf("%d ", f[i]);
	}
	printf("\n");
}

void kmpsearch (const char *t, const int n, const char *p, const int m){
	int f[m];
	buildkmp(p, f, m);
	int s = 0, i = 0;
	while (s <= n - m) {
/*		printf("%c %c|",t[s+i], p[i]);
*/		if (t[s+i] == p[i]) {
			i++;
			if (i == m) {
				printf(">>> found\n");
				return;
			} 
		} 
		else {
/*			printf("\n");
*/			s = s + i - f[i];
			i = f[i] < 0 ? 0 : f[i];
		}
	} 
}

void buildbmh (const char *p, int *l, const int m){
	int i;
	for (i = 0; i < 'z' - 'a'; i++){
		l[i] = m;
	}
	for (i = 0; i < m - 1; i++){
		l[p[i] - 'a'] = m - i - 1;
	}
	for (i = 0; i < 'z' - 'a'; i++){
		if (l[i] != m) printf("(%c, %d)", i+'a', l[i]);
	}
	printf("\n");
}	

void bmhsearch (const char *t, const int n, const char *p, const int m){
	int l['z' - 'a'];
	buildbmh(p, l, m);
}		

void seqsearch(const char *t, const int n, const char *p, const int m){
	int s = 0, i;
	while (s <= n - m) {
		for (i = 0; i < m; i++){
			if (t[s+i] != p[i]) break;
		}
		if (i == m) printf(">>> found\n");
		s++;
	} 
}

int main (int argc, char *argv[]) {
	FILE* pattern = fopen("kmp.txt", "r");
	FILE* text = fopen("test.txt", "r");
	int ch, i = 0, n = 0, size = 2;
	char *p = malloc(size*sizeof(*p));
	char *t = malloc(size*sizeof(*t));
	/* read text */
	while (1) {
		ch = getc(text);
		if (i == size) {
			size*=2;
			t = realloc(t, size*sizeof(*t));
		} 
		if (ch == EOF) {
			t[i] = '\0';
			printf("%s\n", t);
			n = i;
			i = 0;
			size = 2;
			break;
		} else {
			t[i] = ch;
			i++;
		}
	}
	/* read pattern */
	while (1) {
		ch = getc(pattern);
		if (i == size) {
			size*=2;
			p = realloc(p, size*sizeof(*p));
		} 
		if (ch == '\n' || ch == EOF) {
			p[i] = '\0';
			printf("\n");
/*			seqsearch(t, n, p, i);
			kmpsearch(t, n, p, i);
*/			bmhsearch(t, n, p, i);
			i = 0;
		} else {
			p[i] = ch;
			printf(" %c", p[i]);
			i++;
		}
		if (ch == EOF) break;
	}
	free(p);
	return 0;
}
