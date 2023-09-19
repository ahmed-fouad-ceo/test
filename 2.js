const fs = require('fs');

const fileContent = fs.readFileSync('/etc/passwd', 'utf-8');
console.log('File content:', fileContent);
