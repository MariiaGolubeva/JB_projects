// Use "input()" to input a line from the user
// Use "input(str)" to print some text before requesting input
// You will need this in the following stages
const input = require('sync-input')

function isNumber(n) {
    return !isNaN(parseFloat(n)) && !isNaN(n - 0);
}

// The amount of supplies at the beginning
let all_water = 400;
let all_milk = 540;
let all_beans = 120;
let all_cups = 9;
let all_money = 550;

// outputs the remaining supplies
function remaining() {
    console.log(`The machine has:
${all_water} ml of water
${all_milk} ml of milk
${all_beans} g of coffee beans
${all_cups} disposable cups
$${all_money} of money`);
}

// checks if there are enough resources for a particular coffee drink, extracts
// the necessary amount of supplies from the stock, prints a warning if there are
// not enough supplies, or returns to main menu if you type 'back'
function buy() {
    let type = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n');
    if (type == 1) {
        water_need = 250;
        milk_need = 0;
        beans_need = 16;
        coffee_price = 4;
    } else if (type == 2) {
        water_need = 350;
        milk_need = 75;
        beans_need = 20;
        coffee_price = 7;
    } else if (type == 3) {
        water_need = 200;
        milk_need = 100;
        beans_need = 12;
        coffee_price = 6;
    } else if (type === 'back') {
        return;
    } else {
        console.log('Sorry, I don\'t have this position');
        buy();
        return;
    }
    if (all_water >= water_need) {
        if (all_milk >= milk_need) {
            if (all_beans >= beans_need) {
                if (all_cups >= 1) {
                    console.log('I have enough resources, making you coffee!');
                    all_water = all_water - water_need;
                    all_milk = all_milk - milk_need;
                    all_beans = all_beans - beans_need;
                    all_money = all_money + coffee_price;
                    all_cups = all_cups - 1;
                } else {
                    console.log('Sorry, not enough coffee cups!');
                }
            } else {
                console.log('Sorry, not enough coffee beans!');
            }
        } else {
            console.log('Sorry, not enough milk!');
        }
    } else {
        console.log('Sorry, not enough water!');
    }
}

// adds the indicated amount of supplies to the stock
function fill() {
    while (true) {
        new_water = input('Write how many ml of water you want to add. It must be a number:\n');
        if (isNumber(new_water) === true) {
            break;
        }
    }
    while (true) {
        new_milk = input('Write how many ml of milk you want to add. It must be a number:\n');
        if (isNumber(new_milk) === true) {
            break;
        }
    }
    while (true) {
        new_beans = input('Write how many grams of coffee beans you want to add. It must be a number:\n');
        if (isNumber(new_beans) === true) {
            break;
        }
    }
    while (true) {
        new_cups = input('Write how many disposable coffee cups you want to add. It must be a number:\n');
        if (isNumber(new_cups) === true) {
            break;
        }
    }
    all_water = all_water + Number(new_water);
    all_milk = all_milk + Number(new_milk);
    all_beans = all_beans + Number(new_beans);
    all_cups = all_cups + Number(new_cups);
}

// gives up all the money
function take() {
    console.log(`I gave you $${all_money}`);
    all_money = 0;
}

let n = 1;
while (n === 1) {
    let action = input('Write action (buy, fill, take, remaining, exit):\n');
    switch (action) {
        case 'buy':
            buy();
            break;
        case 'fill':
            fill();
            break;
        case 'take':
            take();
            break;
        case 'remaining':
            remaining();
            break;
        case 'exit':
            n = 0;
            break;
    }
}



