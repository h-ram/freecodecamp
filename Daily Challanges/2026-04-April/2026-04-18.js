function findSum(arr, target) {
  const n = arr.length;

  function dfs(i, currentSum, path) {
    if (currentSum === target && path.length >= 2) {
      return path;
    }
    if (i === n) {
      return null;
    }
    let res = dfs(i + 1, currentSum + arr[i], [...path, arr[i]]);
    if (res) {
      return res;
    }
    return dfs(i + 1, currentSum, path);
  }

  const result = dfs(0, 0, []);
  return result ? result : "Sum not found";
}

console.log(findSum([1, 3, 5, 7], 6));
