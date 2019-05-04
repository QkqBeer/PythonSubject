function Person(name, age) {
    this.name = name;
    this.age = age;
}

Person.prototype.setName = function (newName) {
    this.name = newName;
    console.log(this.age)
}

Person.prototype.getName = function () {
    return this.name;
}