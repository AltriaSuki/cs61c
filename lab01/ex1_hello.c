#include <stdio.h>

int main() {
  int var=10;
  int *ptr=&var;
  printf("%p\n",ptr);
  printf("%p\n",&var);
  printf("%p\n",&ptr);

  return 0;
}
