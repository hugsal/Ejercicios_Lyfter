const list1 = ["andres", "maria", "mabel", "nikte", "hugo", "marbella", "eduardo"];
const list2 = [
  "alondra",
  "eduardo",
  "edgar",
  "marbella",
  "camila",
  "hugo",
  "enrique",
];

function printCommonNames(commonList) {
  for (let i = 0; i < commonList.length; i++) {
    console.log(commonList[i]);
  }
}

function commonNames(names1, names2, callback) {
  const matches = [];

  for (let i = 0; i < names1.length; i++) {
    for (let j = 0; j < names2.length; j++) {
      if (names1[i] === names2[j]) {
        matches.push(names1[i]);
        break;
      }
    }
  }

  callback(matches);
}

commonNames(list1, list2, printCommonNames);

