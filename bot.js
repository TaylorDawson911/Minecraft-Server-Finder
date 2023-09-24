const mineflayer = require('mineflayer');

const debug = true;

function create(ip, emailaddress) {
    try {
        const bot = mineflayer.createBot({
            host: ip, // minecraft server ip
            fakeHost: ip,
            email: emailaddress, // username or email
            auth: 'microsoft', // for offline mode servers, you can set this to 'offline'
            version: "1.20.1", // only set if you need a specific version or snapshot
            hideErrors: true, // Disables the console errors
        });

        bot.once('spawn', () => {
            console.log("success");
            bot.quit();
        });

        // Log errors and kick reasons:
        bot.on('kicked', function (reason) {
            if (reason === '{"translate":"multiplayer.disconnect.not_whitelisted"}' || reason === '{"text":"You are not whitelisted on this server!"}') {
                console.log('I\'m not whitelisted on the server!');
            } else if (debug) {
                console.log('I got kicked for the following reason: ' + reason);
            }
        });

        bot.on('error', function (err) {
            if (debug) {
                if (err.code === 'ENOTFOUND') {
                    console.log('Unable to connect to server.');
                } else if (err.code === 'ECONNRESET') {
                    console.log('Connection was reset.');
                } else if (err.code === 'ETIMEDOUT') {
                    console.log('Connection timed out.');
                } else if (err.code === 'ESOCKETTIMEDOUT') {
                    console.log('Socket connection timed out.');
                } else if (err.code === 'ECONNREFUSED') {
                    console.log('Connection refused.');
                } else {
                    console.log('I got an error: ' + err);
                }
            }
        });
    } catch (e) {
        console.log("error", e);
    }
}

const args = process.argv.slice(2);
if (args.length !== 2) {
    console.log('Usage: node app.js <server_ip> <email>');
} else {
    const serverIp = args[0];
    const email = args[1];
    create(serverIp, email);
}
