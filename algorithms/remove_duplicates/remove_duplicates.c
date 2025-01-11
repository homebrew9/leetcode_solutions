/*
 * You are given a string s consisting of lowercase English letters. A duplicate
 * removal consists of choosing two adjacent and equal letters and removing them.
 * We repeatedly make duplicate removals on s until we no longer can.
 * Return the final string after all such duplicate removals have been made. It can
 * be proven that the answer is unique.
 * E.g. "abbaca" => "ca"
 *      "azxxzy" => "ay"
 */
#include <stdio.h>
#define MAXLEN 100

/* Does not work!
char * removeDuplicates(char * s){
    int i, j;
    i = j = 0;
    char *p = s;
    while (p[i]) {
        printf("%c %c\n", *p, p[i]);
        if (p[i] == p[i-1]) {
            printf(">>>> Dupe! at index = [%d]\n", i);
            j = i-2;
            i = i+1;
            while (p[i] && p[i] == p[j]) {
                i++;
                j--;
            }
            p[j+1] = '\0';
        } else {
            i++;
        }
    }
    return s;
}
*/

// The solution below was by user "bbulkow". Looks pretty good!
char * removeDuplicates(char * S){
    if (*S == 0) return(S);

    int dstOff = 0; // behind
    int srcOff = 0; // forward

    while (S[srcOff]) {
        printf(">> %3d, %c, %3d, %c\n", srcOff, S[srcOff], dstOff, S[dstOff]);
        if (S[srcOff] == S[srcOff+1]) {
            srcOff += 2;
        }
        else if ((dstOff > 0) && (dstOff != srcOff) && (S[dstOff-1] == S[srcOff])) {
            srcOff++;
            dstOff--;
        }
        else {
            if (dstOff != srcOff) {
                S[dstOff] = S[srcOff];
            }
            dstOff++;
            srcOff++;
        }
    }
    S[dstOff] = 0;

    return(S);
}

int main() {
    //char str[MAXLEN] = "abcdeffedcxx";
    //char str[MAXLEN] = "abcdeffedcxy";
    //char str[MAXLEN] = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba";
    //char str[MAXLEN] = "abcdefghijklmnopqrstuvwxyzQzyxwvutsrqponmlkjihgfedcba";
    //char str[MAXLEN] = "abcxyzwwzyxdef";
    //char str[MAXLEN] = "xyzwwzyxdef";
    //char *ptr = str;
    //printf("Original: [%s]\n", ptr);
    //removeDuplicates(ptr);
    //printf("Modified: [%s]\n", ptr);
    char *p;
    char arr[10][MAXLEN] = {
                            "abcdeffedcxx",
                            "abcdeffedcxy",
                            "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba",
                            "abcdefghijklmnopqrstuvwxyzQzyxwvutsrqponmlkjihgfedcba",
                            "abcxyzwwzyxdef",
                            "",
                            "a",
                            "abb",
                            "mnoxyzwwzyx",
                            "xy"
                           };
    for (int i = 0; i < 10; i++) {
        printf("%s\n", "======================================================");
        p = arr[i];
        printf("Original : [%s]\n", p);
        removeDuplicates(p);
        printf("Modified : [%s]\n", p);
    }
}

