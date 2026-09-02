function wait(seconds) {
  return new Promise((resolve) => {
    setTimeout(() => {
      console.log(`Han pasado ${seconds} segundos`);
      resolve(seconds);
    }, seconds * 1000);
  });
}

async function main() {
  await wait(2);
  await wait(3);
  await wait(1);
}

main();
