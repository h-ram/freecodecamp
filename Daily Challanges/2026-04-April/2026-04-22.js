const SCORE = {
  "bottle": 10,
  "can": 6,
  "bag":8,
  "tire": 35,
  "straw": 4, 
  "cardboard": 3,
  "newspaper": 3,
  "shoe": 12,
  "electronics": 25,
  "battery": 18,
  "mattress": 38
}

function getCleanupScore(items) {
  let final_score = 0
  let streak = 0
  let prev = null
  for (let i = 0; i < items.length; i++) {
    let value = 0
    let isRare = Array.isArray(items[i])
    if (isRare) {
      value = items[i][1]
      streak = 0
      prev = null
    } else {
      if (items[i] === prev) streak++
      else streak = 1

      value = SCORE[items[i]] + (streak - 1)
      prev = items[i]
    }
    let multiplier = 1
    if ((i + 1) % 5 === 0) {
      multiplier = (i + 1) / 5 + 1
    }
    final_score += value * multiplier
  }

  return final_score
}

console.log(getCleanupScore(["bottle", "straw", "shoe", "battery"]))
console.log(getCleanupScore(["electronics", "straw", "newspaper", "bottle", "bag"]))
console.log(getCleanupScore(["shoe", "can", "can", "can", "bottle", "bottle", "straw", "straw", "straw"]))
console.log(getCleanupScore(["mattress", ["rare", 80], "tire", "tire", "tire", ["rare", 95]]))