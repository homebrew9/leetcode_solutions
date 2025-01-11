#include <stdio.h>
#include <string.h>
#define NUM_STRINGS 5
#define MAX_LENGTH 100

char* reverse_chars(char *s, char *left, char *right) {
    char temp;
    while (left < right) {
        temp = *left;
        *left = *right;
        *right = temp;
        left++;
        right--;
    }
    return s;
}

char* reverse_words(char *p) {
    char *lag, *lead;
    lead = p;
    lag = p;
    int len = 0;
    while (1) {
        if (*lead == '\0') {
            p = reverse_chars(p, lag, lead-1);
            break;
        } else if (*lead == ' ') {
            p = reverse_chars(p, lag, lead-1);
            lag = lead + 1;
        }
        lead++;
        len++;
    }
    p = reverse_chars(p, p, lead-1);
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

    char *q;
    char arr[NUM_STRINGS][MAX_LENGTH] = {
        "hello there my friend",
        "the cat sat on the mat",
        "the woods are lovely",
        "now is a good time for all young men to come to the aid of their country",
        " all the devils are here "
    };
    for (int i = 0; i < NUM_STRINGS; i++) {
        printf("Original string = [%s]\n", arr[i]);
        q = reverse_words(arr[i]);
        printf("Return string   = [%s]\n", q);
        printf("==================================================\n");
    }

    return 0;
}


