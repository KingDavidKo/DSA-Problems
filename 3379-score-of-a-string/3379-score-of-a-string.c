int scoreOfString(char* s) {
    int i = 1;
    int sum = 0;
    while (s[i]) {
        sum += abs(s[i] - s[i-1]);
        i++;
    }
    return sum;
}