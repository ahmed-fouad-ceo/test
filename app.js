const regex = /^([a-zA-Z]+)*$/;

const input = 'a'.repeat(25) + '!'; // This input can trigger ReDoS

if (regex.test(input)) {
  console.log('Valid input');
} else {
  console.log('Invalid input');
}
