from flask import Flask, request, jsonify
import mysql.connector as MC

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <form action="/search" method="post">
            <input type="text" name="query" id="query" placeholder="Search...">
            <input type="submit" value="Search">
        </form>
        <script>
            document.getElementById('query').addEventListener('input', function() {
                fetch('/search', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({query: this.value})
                }).then(response => response.json())
                .then(data => console.log(data));
            });
        </script>
    '''

@app.route('/search', methods=['POST'])
def search():
    query = request.json.get('query', '')
    conn = MC.connect(
        host="mariadb",
        user="root",
        password="",
        database="elgoog"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM urls WHERE title LIKE %s OR description LIKE %s", ('%' + query + '%', '%' + query + '%'))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(rows)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
