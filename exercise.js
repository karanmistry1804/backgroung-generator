//let + const
const a = "test";
let b = true;
const c = 789;

a = "test2";

//Destructuring
const person = {
	firstName:"Karan",
	lastName:"Mistry",
	age:19,
	eyeColor:"blue"
};

const firstName=person.firstName;
const lastName=person.lastName;
const age=person.age;
const eyeColor=person.eyeColor;

//Object properties
const a="test";
const b=225;
let c=true;

const obj={
	a:a,
	b:b,
	c:c
}

//Templete strings
const firstName="Karan";
const city="Godhra";
const message = `Hello ${firstName} have I met you before? I think we met in ${city} last summer no????`;

//Symbol
const new1=Symbol("This is my first symbol");

//Arrow Function
const arrow=(username,location) => {
	if(username && location){
		return "I am not lost";
	}
	else{
		return "I am totally lost!";
	}
}

//ADVANCED FUNCTIONS 
//Closure 
const addTo = x => y => x + y;
const addToTen = addTo(10);
addToTen(3);

//Currying
const sum = (a,b) => a + b;
const curriedSum = (a) = (b) = a + b;
const add5 = curriedSum(5)
add5(12)

//Currying
const sum = (a,b) => a + b;
const curriedSum = (a) = (b) = a + b;
curriedSum(30)(2)

// Composing
const compose = (f,g) => (a) => f(g(a));
const add1 = (num) => num + 1;
const add5 = (num) => num + 5;
compose(add1,add5)(10) 

//ADVANCED ARRAY
// Complete the below questions using this array:
const array = [
     {
     	username:"John",
     	team:"red",
     	score:5,
     	items:["ball","book","pen"]
     },
     {
     	username:"Becky",
     	team:"blue",
     	score:10,
     	items:["tape","backpack","pen"]
     },
     {
     	username:"susy",
     	team:"red",
     	score:55,
     	items:["ball","eraser","pen"]
     },
     {
     	username:"tyson",
     	team:"green",
     	score:1,
     	items:["book","pen"]
     }          
];

const newName = [];
const foreachName = array.forEach((array[username]) => {
	newName.push(array[username] );
})
console.log(newName);