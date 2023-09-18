const lodash = require('lodash');

const data = { user: 'Snyk' };
const clone = lodash.clone(data);

console.log(clone);
