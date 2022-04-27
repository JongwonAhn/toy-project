const path = require('path');
const os = require('os');
const fs = require('fs');

const folder = process.argv[1];
const workingDir = path.join(os.homedir(), 'pictures', folder);

if(!folder || !fs.existsSync(workingDir)) {
    console.error('please enter folder name in pictures');
    // return;
}


const videoDir = path.join(workingDir, 'video');
const capturedDir = path.join(workingDir, 'captured');
const duplicatedDir = path.join(workingDir, 'duplicated');

!fs.existsSync(videoDir) && fs.mkdirSync('videoDir');
!fs.existsSync(capturedDir) && fs.mkdirSync('capturedDir');
!fs.existsSync(duplicatedDir) && fs.mkdirSync('duplicatedDir');

fs.promises.readdir
