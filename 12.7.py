function formatPhoneNumber(phoneNumber) {
    let first = phoneNumber.slice(0, 3);
    let second = phoneNumber.slice(3, 6);
    let third = phoneNumber.slice(6, 10);

    
    return `(${first}) ${second}-${third}`;
}


let output = formatPhoneNumber("8008461212");
console.log(output);
