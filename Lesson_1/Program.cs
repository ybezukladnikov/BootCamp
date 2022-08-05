// int [] array1 = {45, 5, 3, 2, 5, 6, -3, 34, 7};

// DateTime dt1 = DateTime.Now; 

// for (int i =0 ; i<array1.Length; i++)
// {
//     for(int j=0; j < array1.Length-1;j++)
//     {
//         if (array1[j]>array1[j+1])
//         {
//             int temp = array1[j];
//             array1[j] = array1[j+1];
//             array1[j+1] = temp;
//         }
//     }
// }

// Console.WriteLine((DateTime.Now - dt1).TotalMilliseconds);

// int [] array2 = {45, 5, 3, 2, 5, 6, -3, 34, 7};

// DateTime dt = DateTime.Now; 

// for (int i =0; i<array2.Length-1; i++)
// {
//     int minIndex = i;
//     for(int j = i+1; j<array2.Length; j++)
//     {
//         if(array2[j]<array2[minIndex])
//             minIndex= j;
//     }

//     int temp = array2[i];
//     array2[i] = array2[minIndex];
//     array2[minIndex] = temp;
// }

// Console.WriteLine((DateTime.Now - dt).TotalMilliseconds);




// int n =5;

// int [] array = {1,2,3,4,5,6,7,8};
// Console.WriteLine(string.Join(" ", array));
// int sizeArray = array.Length;
// int [] temp = new int[n];

// int j = sizeArray;
// for (int i = n-1; i >=0; i--)
// {
//     temp[i] = array[j-1];
//     j--;
// }



// for(int k = 0; k<n; k++)
// {
//     for(int i = array.Length-1; i != 0; i--)
//     {
//         array[i] = array[i-1];
//     }
// }

// for(int d = 0; d<n; d++)
// {
//     array[d] = temp[d];
// }


// Console.WriteLine(string.Join(" ", array));

int n =2;

int [] array = {1,2,3,4,5};
int [] temp = new int[n];

Console.WriteLine(2+3);