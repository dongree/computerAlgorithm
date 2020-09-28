#include <stdio.h>


void merge(int list[], int left, int mid, int right){
	
	int i = left, j = mid + 1, k = left;
	int sorted[right+1];
	
	while(i<=mid && j<=right){
		if(list[i] <= list[j]){
			sorted[k] = list[i++];
		}else{
			sorted[k] = list[j++];
		}
		k++;
	}
	while(i<=mid){
		sorted[k++] = list[i++];
	} 
    while(j<=right){
    	sorted[k++] = list[j++];
	} 
	for(int t=left; t<=right; t++){
		list[t] = sorted[t];
	}
}


void merge_sort(int list[], int left, int right){
	int mid;
	if (left < right){
		mid = (left + right) / 2;
		merge_sort(list, left, mid);
		merge_sort(list, mid + 1, right);
		merge(list, left, mid, right);
	}
}


int main(){
	int n;
	
	printf("please input a number : ");
	scanf("%d\n", &n);
	
	int arr[n];
	
	for(int i=0; i<n; i++){
		scanf("%d", &arr[i]);
	}
	
	merge_sort(arr, 0, n);
	
	for(int k=0; k<n; k++){
		printf("%d ", arr[k]);
	}
	
	return 0;
}
