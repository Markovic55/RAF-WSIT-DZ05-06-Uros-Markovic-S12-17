from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/raspored')
def raspored():
	f = open("src/RAFraspored.csv", "r")
	redovi = f.readlines()
	svi_predavaci = [red.split(',')[2] for red in redovi]
	
	jedinstveni_predavaci=[]
	for predavac in svi_predavaci:
		if predavac not in jedinstveni_predavaci:
			jedinstveni_predavaci.append(predavac)
	
	svi_predavaci = jedinstveni_predavaci.sort()

	sve_ucionice=[red.split(',')[6] for red in redovi]
	jedinstvene_ucionice=[]
	for ucionica in sve_ucionice:
		if ucionica not in jedinstvene_ucionice:
			jedinstvene_ucionice.append(ucionica)

	sve_ucionice = jedinstvene_ucionice.sort()

	



	return  render_template("raspored.html", redovi= redovi, svi_predavaci=jedinstveni_predavaci,
	 sve_ucionice=jedinstvene_ucionice )



if __name__ == '__main__':
	app.run()