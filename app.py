from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


maps = [['kh', 'x'],['Kh', 'X'], ['ch', 'tr'],['Ch', 'Tr'],['c', 'k'],['C', 'K'],['tr', 'c'],['Tr', 'C'], ['gi', 'z'],['Gi', 'Z'], ['d', 'z'],['D', 'Z'],  ['r', 'z'],['R', 'Z'], ['đ', 'd'],['Đ', 'D'], ['ph', 'f'],['Ph', 'F'], ['q', 'k'],['Q', 'K'], ['ng', 'q'],['Ng', 'Q'], ['gh', 'g'],['Gh', 'G'], ['th', 'w'],['Th', 'W'],  ['nh', 'n\''],['Nh', 'N\'']]

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/ajax', methods=['POST'])
def ajax():
	input_data = request.form['input_text']
	for i in maps:
		if i[0] in input_data:
			input_data = input_data.replace(i[0],i[1])
	return jsonify({'result': input_data})
if __name__ == '__main__':
	app.run(debug=True)


