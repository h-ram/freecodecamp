function fixPrankNumber(nums) {
  const n = nums.length;
  const diffs = [];
  for (let i = 0; i < n - 1; i++) diffs.push(nums[i + 1] - nums[i]);

  const freq = {};
  diffs.forEach((d) => (freq[d] = (freq[d] || 0) + 1));
  const step = Number(Object.entries(freq).sort((a, b) => b[1] - a[1])[0][0]);

  for (let i = 0; i < n - 1; i++) {
    if (diffs[i] !== step) {
      for (const bad of [i, i + 1]) {
        const result = [...nums];
        result[bad] = bad > 0 ? result[bad - 1] + step : result[bad + 1] - step;
        if (
          result.every((_, j) => j === 0 || result[j] - result[j - 1] === step)
        ) {
          return result;
        }
      }
    }
  }

  return [...nums];
}
