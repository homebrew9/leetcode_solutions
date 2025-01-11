#include <stdio.h>
#include <string.h>
#define MAX 5
#define LEN 100

char* reverse_chars(char *s, char *left, char *right) {
    //printf("    >> Start of reverse_chars, s = [%s]\n", s);
    char temp;
    while (left < right) {
        //printf("        >> (left, right) = (%X, %X) ; (%c, %c)\n", left, right, *left, *right);
        temp = *left;
        //printf("            >> 1: (temp, left, right) = (%X, %X, %X) ; (%c, %c, %c)\n", &temp, left, right, temp, *left, *right);
        *left = *right;
        //printf("            >> 2: (temp, left, right) = (%X, %X, %X) ; (%c, %c, %c)\n", &temp, left, right, temp, *left, *right);
        *right = temp;
        //printf("            >> 3: (temp, left, right) = (%X, %X, %X) ; (%c, %c, %c)\n", &temp, left, right, temp, *left, *right);
        left++;
        right--;
    }
    //printf("    >> End of reverse_chars, s   = [%s]\n", s);
    return s;
}

char* reverse_words(char *p) {
    char *lag, *lead;
    lead = p;
    lag = p;
    int len = 0;
    while (1) {
        //printf("[%c]\n", *lead);
        if (*lead == '\0') {
            p = reverse_chars(p, lag, lead-1);
            break;
        } else if (*lead == ' ') {
            //printf(">> Now calling reverse_chars\n");
            p = reverse_chars(p, lag, lead-1);
            lag = lead + 1;
        }
        lead++;
        len++;
    }
    //printf("strlen = [%d]\n", len);
    //printf("p      = [%s]\n", p);
    p = reverse_chars(p, p, lead-1);
    //printf("p      = [%s]\n", p);
    return p;
}

int main() {
/*
    //char str[] = "hello there my friend";
    //char str[] = "the cat sat on the mat";
    //char str[] = "the woods are lovely";
    //char str[] = "now is a good time for all young men to come to the aid of their country";
    char str[] = " all the devils are here ";
    char *q, *p;
    p = str;
    printf("Original string = [%s]\n", p);
    q = reverse_words(p);
    printf("Return string   = [%s]\n", q);
    printf("==================================================\n");
*/

    char *q, *p;
    char s[LEN];
    char *arr[MAX] = {
                        "hello there my friend",
                        "the cat sat on the mat",
                        "the woods are lovely",
                        "now is a good time for all young men to come to the aid of their country",
                        " all the devils are here "
                     };
    for (int i = 0; i < MAX; i++) {
        p = (char *)arr[i];
        printf("Original string = [%s]\n", arr[i]);
        strcpy(s, arr[i]);
        //q = reverse_words(arr[i]);
        q = reverse_words(s);
        printf("Return string   = [%s]\n", q);
        printf("==================================================\n");
    }

    return 0;
}

