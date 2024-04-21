// Функция для отправки запроса с заданной датой
async function sendRequest(submission) {
    const url = 'link for abuse';
    const headers = {
        'User-Agent': 'your headers'
    };

    const body = JSON.stringify({
        challenge_id: 22,
        submission: `CIT{${submission}}`
    });

    const response = await fetch(url, {
        method: 'POST',
        headers: headers,
        credentials: 'include',
        mode: 'cors',
        body: body
    });

    const data = await response.json();
    console.log(`Sent request for date: ${submission}, Response:`, data);
}

// only my task
function generateDates() {
    const dates = [];
    for (let year = 2000; year <= 2024; year++) {
        for (let month = 1; month <= 12; month++) {
            for (let day = 1; day <= 31; day++) {
                const date = `${month.toString().padStart(2, '0')}/${day.toString().padStart(2, '0')}/${year}`;
                dates.push(date);
            }
        }
    }
    return dates;
}

// Вызов функции для генерации дат и отправки запросов
const dates = generateDates();
dates.forEach(date => sendRequest(date));
