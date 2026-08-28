const student = {
  name: "John Doe",
  grades: [
    { name: "math", grade: 80 },
    { name: "science", grade: 100 },
    { name: "history", grade: 60 },
    { name: "PE", grade: 90 },
    { name: "music", grade: 98 },
  ],
};

const { name, grades } = student;

const gradeAvg =
  grades.reduce((accumulator, current) => accumulator + current.grade, 0) /
  student.grades.length;

grades.sort((a, b) => {
  if (a.grade > b.grade) {
    return 1;
  }
  if (a.grade < b.grade) {
    return -1;
  }
  return 0;
});

const highestGrade = grades.pop();
const lowestGrade = grades.shift();

console.log({
  name,
  gradeAvg,
  highestGrade: highestGrade.name,
  lowestGrade: lowestGrade.name,
});
