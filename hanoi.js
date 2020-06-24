function main() {
  // Пятнадцать дисков, лол.
  hanoi(15, 1, 2)
}

function hanoi(n, i, k) {
  if (n == 1) {
    console.log(`Move disk ${n} from pin ${i} to ${k}`)
  } else {
    const tmp = 6 - i - k
    hanoi(n - 1, i, tmp)
    console.log(`Move disk ${n} from pin ${i} to ${k}`)
    hanoi(n - 1, tmp, k)
  }
}

main()