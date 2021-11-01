from flask import Flask, render_template


ungdung = Flask(__name__)

@ungdung.route('/')
def trangchu():
    return '<b> Xin chao</b> <i>cac ban!</i>'


@ungdung.route('/abc')
def trangabc():
    #return '<h1> hello </h1>'
    return render_template('hello.html')# file webhtml.html này phải để bên trong thư mục templates


@ungdung.route('/py')
def trangpython():
    return 'Chúc mừng các bạn!'

if __name__ == "__main__":
    ungdung.run(port=5151) # mac dinh la cong 5000

