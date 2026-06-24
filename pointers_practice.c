int values[5] = {100, 200, 300, 400, 500};
int *p = values;

printf("ptr points to: %d\n", *ptr);     // 10
ptr++;  
printf("ptr now points to: %d\n", *ptr); // 20
ptr ++; 
printf("ptr now points to: %d\n", *ptr); // 30
ptr ++;
printf("ptr points to: %d\n", *ptr);     // 40
ptr++;  
printf("ptr now points to: %d\n", *ptr); // 50

