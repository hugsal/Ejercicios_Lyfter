const fs = require("fs");

fs.readFile("firstFile.txt", "utf8", (_, data) => {
  const firstFile = data.split("\n");
  fs.readFile("secondFile.txt", "utf8", (_, data) => {
    const secondFile = data.split("\n");
    const common = firstFile.filter((element) => secondFile.includes(element));
    console.log(common.join(" "));
  });
});
