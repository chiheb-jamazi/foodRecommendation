from flask import Flask, render_template, request
import psycopg2


app = Flask(__name__)


POSTGRESSQL_URI = "postgres://iqnieopb:0qJBYcbuo9Vm1hHVi1FxsBkVVuyGjQeL@hattie.db.elephantsql.com/iqnieopb"
connection = psycopg2.connect(POSTGRESSQL_URI)

try:
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(
                "CREATE TABLE transaction ( date TEXT, plat_sale_sucre TEXT , plat_chaud_froid TEXT ,plat_pates_non_pates TEXT, carnivore_vegetarien TEXT,diabetique_non_diabetique TEXT);"
            )
except psycopg2.errors.DuplicateTable:
    pass


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        print(request.form)
        with connection:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO transaction values (%s,%s,%s,%s,%s,%s);",
                               (
                                   request.form.get("date"),
                                   request.form.get("plat_sale_sucre"),
                                   request.form.get("plat_chaud_froid"),
                                   request.form.get("plat_pates_non_pates"),
                                   request.form.get("carnivore_vegetarien"),
                                   request.form.get("diabetique_non_diabetique"),
                               ),
                               )
    return render_template("form.html")


@app.route("/transactions")
def show_transactions():
    food = {"apple_pie", "baby_back_ribs", "baklawa", "breakfast_burrito", "caesar_salad", "cheesecake"
        , "chicken_curry", "chicken_quesadilla", "chicken_wings", "chocolate_cake", "chocolate_mousse", "churros"
        , "club_sandwich", "croque_madame", "donuts", "edamame", "fish_and_chips", "french_fries", "fried_rice"
        , "garlic_bread", "hamburger", "hot_and_sour_soup", "ice_cream", "lasagna", "macaroni_and_cheese", "macarons",
            "omelette",
            "koskos", "pancakes", "pizza", "samosa", "scallops", "shrimp_and_grits", "spaghetti_bolognese", "steak",
            "waffles"}
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * From TRANSACTION ;")
            transactions = cursor.fetchall()
            last_elements = transactions[-1]
            preference = last_elements[1:]
            for i in preference:
                if i == 'Sucré':
                    food.discard('baby_back_ribs')
                    food.discard('breakfast_burrito')
                    food.discard('caesar_salad')
                    food.discard('chicken_curry')
                    food.discard('chicken_quesadilla')
                    food.discard('chicken_wings')
                    food.discard('club_sandwich')
                    food.discard('croque_madame')
                    food.discard('edame')
                    food.discard('fish_and_chips')
                    food.discard('french_fries')
                    food.discard('fried_rice')
                    food.discard('garlic_bread')
                    food.discard('hamburger')
                    food.discard('hot_and_sour_soup')
                    food.discard('lasagna')
                    food.discard('macaroni_and_cheese')
                    food.discard('omelette')
                    food.discard('koskos')
                    food.discard('pizza')
                    food.discard('scallops')
                    food.discard('shrimp_and_grits')
                    food.discard('spaghetti_bolognese')
                    food.discard('steak')
                if i == 'Salé':
                    food.discard('apple_pie')
                    food.discard('baklawa')
                    food.discard('cheesecake')
                    food.discard('chocolate_cake')
                    food.discard('chocolate_mousse')
                    food.discard('donuts')
                    food.discard('ice_cream')
                    food.discard('macarons')
                    food.discard('pancakes')
                    food.discard('fish_and_chips')
                    food.discard('waffles')
                    food.discard('samosa')

                if i == 'Plat Froid':
                    food.discard('chicken_curry')
                    food.discard('fish_and_chips')
                    food.discard('lasagna')
                    food.discard('hot_and_sour_soup')
                    food.discard('omelette')
                    food.discard('koskos')
                    food.discard('pizza')
                    food.discard('scallops')
                    food.discard('chicken_quesadilla')
                    food.discard('spaghetti_bolognese')
                    food.discard('steak')
                    food.discard('baby_back_ribs')
                    food.discard('breakfast_burrito')
                    food.discard('chicken_wings')
                    food.discard('croque_madame')
                    food.discard('french_fries')
                    food.discard('fried_rice')
                    food.discard('hamburger')
                    food.discard('macaroni_and_cheese')
                    food.discard('shrimp_and_grits')

                if i == 'Plat Chaud':
                    food.discard('apple_pie')
                    food.discard('baklawa')
                    food.discard('caesar_salad')
                    food.discard('cheesecake')
                    food.discard('chocolate_cake')
                    food.discard('chocolate_mousse')
                    food.discard('churros')
                    food.discard('club_sandwich')
                    food.discard('croque_madame')
                    food.discard('donuts')
                    food.discard('ice_cream')
                    food.discard('macarons')
                    food.discard('pancakes')
                    food.discard('samosa')
                    food.discard('waffles')

                if i == 'Pas de pates':
                    food.discard('apple_pie')
                    food.discard('breakfast_burrito')
                    food.discard('club_sandwich')
                    food.discard('croque_madame')
                    food.discard('garlic_bread')
                    food.discard(' hamburger')
                    food.discard('lasagna')
                    food.discard('pancakes')
                    food.discard('macaroni_and_cheese')
                    food.discard(' koskos')
                    food.discard('chicken_quesadilla')
                    food.discard('pizza')
                    food.discard('spaghetti_bolognese')
                    food.discard('chocolate_cake')
                    food.discard('churros')
                    food.discard('donuts')
                    food.discard('waffles')
                if i == 'diabétique':
                    food.discard('apple_pie')
                    food.discard('baklawa')
                    food.discard('cheesecake')
                    food.discard('chocolate_cake')
                    food.discard('chocolate_mousse')
                    food.discard('ice_cream')
                    food.discard('macarons')
                    food.discard('pancakes')
                    food.discard('samosa')
                    food.discard('waffles')
                    food.discard('donuts')
                if i == 'Vegan' or 'Vegetarien':
                    food.discard('baby_back_ribs')
                    food.discard('breakfast_burrito')
                    food.discard('chicken_curry')
                    food.discard('chicken_quasadilla')
                    food.discard('chicken_wings')
                    food.discard('club_sandwich')
                    food.discard('fish_and_chips')
                    food.discard('hamburger')
                    food.discard('lasagna')
                    food.discard('koskos')
                    food.discard('scallops')
                    food.discard('shrimp_and_grits')
                    food.discard('spaghetti_bolognese')
                    food.discard('steak')

                if i == 'Carnivore':
                    food.discard('baby_back_ribs')
                    food.discard('breakfast_burrito')
                    food.discard('chicken_curry')
                    food.discard('chicken_quasadilla')
                    food.discard('chicken_wings')
                    food.discard('club_sandwich')
                    food.discard('fish_and_chips')
                    food.discard('hamburger')
                    food.discard('lasagna')
                    food.discard('koskos')
                    food.discard('scallops')
                    food.discard('shrimp_and_grits')
                    food.discard('spaghetti_bolognese')
                    food.discard('steak')
            elements = food

    return render_template("transactions.jinja2", entries=elements)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
