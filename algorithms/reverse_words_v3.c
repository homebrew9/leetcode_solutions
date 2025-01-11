#include <stdio.h>
#include <string.h>
#define NUM_STRINGS 5
#define MAX_LENGTH 300

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

char* reverse_words_orig(char *p) {
    char *lag, *lead;
    lead = p;
    lag = p;
    int len = 0;
    int leading_spaces_found = 0;
    int first_time = 0;
    int is_first_nonspace = 1;
    while (*lead == ' ') {
        if (leading_spaces_found == 0) {
            leading_spaces_found = 1;
        }
        //printf("[%X|%c]\n", lead, *lead);
        lead++;
    }
    //printf("====\n");
    while (1) {
        //if (*lead == '\0') {
        //    p = reverse_chars(p, lag, lead-1);
        //    break;
        //} else if (*lead == ' ') {
        //    p = reverse_chars(p, lag, lead-1);
        //    lag = lead + 1;
        //}
        if (*lead == '\0') {
            break;
        }
        //printf("[%X|%c]\n", lead, *lead);
        if (*lead != ' ') {
            if (*(lead - 1) == ' ') {
                if (first_time == 0) {
                   //printf("\t\t>> first_time = [%d] ; leading_spaces_found = [%d] ; no space assigned to lag...\n", first_time, leading_spaces_found);
                   if (leading_spaces_found == 0) {
                       *lag = ' ';
                       lag++;
                   }
                   first_time = 1;
                } else {
                   //printf("\t\t>> i should assign a space to lag and increment it here...\n");
                   *lag = ' ';
                   lag++;
                }
            }
            *lag = *lead;
            lag++;
        }
        lead++;
        //len++;
    }
    *lag = '\0';
    //p = reverse_chars(p, p, lead-1);
    return p;
}

void reverse_seq(char *begin, char *end) {
    char *p, *q;
    char temp;
    p = begin;
    q = end;
    while (p < q) {
        //printf("\t>>> (%c, %c)\n", *p, *q);
        temp = *p;
        *p = *q;
        *q = temp;
        p++;
        q--;
    }
}

void adjust_string(char *begin, char *end, char *writer) {
    char *p, *q;
    p = begin;
    q = end;
    while (p <= q) {
        //printf("\t\t>>[%X|%c]\n", writer,*writer);
        *writer = *p;
        p++;
        writer++;
    }
    writer--;
}

char* reverse_words(char *p) {
    char *left, *right, *final, *origin;
    left = p;
    right = p;
    final = p;
    origin = p;
    while (*right == ' ') {
        right++;
        left++;
    }

    int in_word = 0;
    int in_space = 0;
    char *iter;
    while (1) {
        //printf("[%X|%c]\n", right,*right);
        if (*right == '\0') {
            //printf("==>> [%X|%c], [%X|%c]\n", left,*left,right,*right);
            //if (*left != ' ') {
            //    for (iter = right-1; iter >= left; iter--) {
            //        *final = *iter;
            //        printf("\t>>> (%c)\n", *final);
            //        final++;
            //    }
            //    *final = ' ';
            //    printf("\t>>> (%c)\n", *final);
            //    final++;
            //    left = right;
            //}

            if (*left != ' ') {
                reverse_seq(left, right-1);
                while (left < right) {
                    *final = *left;
                    left++;
                    final++;
                }
                *final = ' ';
                final++;
            }
            break;
        }
        if (*right != ' ' && in_word == 0) {
            in_word = 1;
            left = right;
        } else if (in_word == 1) {
            if (*right == ' ') {
                //for (iter = right-1; iter >= left; iter--) {
                //    *final = *iter;
                //    printf("\t>>> (%c, %c)\n", *iter, *final);
                //    final++;
                //}

                //iter = right - 1;
                //while (iter >= left) {
                //    *final = *iter;
                //    printf("\t>>> iter, final = [%X|%c], [%X|%c]\n", iter,*iter,final,*final);
                //    iter--;
                //    final++;
                //}
                //*final = ' ';
                //printf("\t>>> final = (%c)\n", *final);
                //final++;
                //left = right;

                reverse_seq(left, right-1);
                while (left < right) {
                    *final = *left;
                    left++;
                    final++;
                }
                *final = ' ';
                final++;

                in_word = 0;
                in_space = 1;
            }
        }

        if (*right == ' ' && in_space == 0) {
            in_space = 1;
        } else if (in_space == 1) {
            if (*right != ' ') {
                left = right;
                in_space = 0;
                in_word = 1;
            }
        }

        right++;
    }
    final--;
    *final = '\0';
    reverse_seq(origin, final-1);
    return p;
}

int main() {
    char *q;
    char arr[NUM_STRINGS][MAX_LENGTH] = {
        "    hello   there my  friend   ",
        "the sky is blue",
        "the woods are lovely    ",
        "now     is    a good time for all young                  men to come to the  aid   of    their     country",
        "all the devils are here"
    };
    for (int i = 0; i < NUM_STRINGS; i++) {
        printf("Original string = [%s]\n", arr[i]);
        q = reverse_words(arr[i]);
        printf("Return string   = [%s]\n", q);
        printf("==================================================\n");
    }
    return 0;
}

