import redis from 'redis';

const client = redis.createClient({
  url: 'redis://127.0.0.1:6379'
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, redis.print);
};

const displaySchoolValue = (schoolName) => {
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.log(`Error retrieving value: ${err}`);
    } else {
      console.log(reply);
    }
  });
};

displaySchoolValue('Holberton');

// Set a new value for 'HolbertonSanFrancisco'
setNewSchool('HolbertonSanFrancisco', '100');

// Display the value for 'HolbertonSanFrancisco'
displaySchoolValue('HolbertonSanFrancisco');
