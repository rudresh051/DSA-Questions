class Solution {
  merge(arr, l, m, r) {
    // Your code here
    var n1 = m - l + 1;
    var n2 = r - m;
    //  Create temp arrays
    var L = new Array(n1);
    var R = new Array(n2);
    // copy data to temp arrays
    for (var i = 0; i < n1; i++) {
      L[i] = arr[l + i];
    }
    for (var j = 0; j < n2; j++) {
      R[j] = arr[m + 1 + j];
    }
    var k = l;
    while (i < n1 && j < n2) {
      if (L[i] <= R[j]) {
        arr[k] = L[i];
        i++;
      } else {
        arr[k] = R[j];
      }
      k++;
    }
    // Copy remaining elements of L[] if any
    while (i < n1) {
      arr[k] = L[i];
      i++;
      k++;
    }
    // Copy remaining elements of R[] if any
    while (j < n2) {
      arr[k] = R[j];
      j++;
      k++;
    }
  }

  mergeSort(arr, l, r) {
    //code here
    if (l < r) {
      var m = Math.floor((l + r) / 2);
      this.mergeSort(arr, l, m);
      this.mergeSort(arr, m + 1, r);
      this.merge(arr, l, m, r);
    }
  }
}
