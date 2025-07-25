const { spawn } = require('child_process');
const fs = require('fs');

const logFile = fs.createWriteStream('dev-server-output.log', { flags: 'a' });

console.log('Starting npm run dev...');
const dev = spawn('npm', ['run', 'dev']);

dev.stdout.on('data', (data) => {
  process.stdout.write(data);
  logFile.write(data);
});

dev.stderr.on('data', (data) => {
  process.stderr.write(data);
  logFile.write(data);
});

dev.on('close', (code) => {
  console.log(`npm run dev exited with code ${code}`);
  logFile.write(`\nnpm run dev exited with code ${code}\n`);
  logFile.end();
});

// Handle Ctrl+C gracefully
process.on('SIGINT', () => {
  console.log('Received SIGINT, closing log file.');
  logFile.end();
  process.exit();
}); 