from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/enviar", methods=['GET'])
def bot():
    escolha = request.args.get('escolha')
    if escolha == '1':
        return render_template('index.html', msg='clique aqui para ir ao portal acadêmico onde voçê poderá visualizar suas faltas, informe sua matricula e senha', link='https://uniateneu.itvix.com.br/FrameHTML//web/app/edu/PortalEducacional/#/faltas',
        msg1="Em relaçao as suas notas clique aqui", link1=" https://uniateneu.itvix.com.br/FrameHTML//web/app/edu/PortalEducacional/#/notas")
    elif escolha == '2':
        return render_template('index.html', msg="clique aqui para ir ao portal acadêmico onde voçê poderá visualizar os boletos pagos e pendentes", link="https://uniateneu.itvix.com.br/FrameHTML//web/app/edu/PortalEducacional/#/financeiro",
         msg1="Caso queira renegociar o valor de alguma matricula clique aqui", link1="https://uniateneu.itvix.com.br/FrameHTML//web/app/edu/PortalEducacional/#/negociacao/listagem-debitos-financeiro")
    elif escolha == '3':
        return render_template('index.html', msg='clique aqui onde ele lhe encaminhará para o portal do aluno, informe sua matrícula e senha, vá na opção horario e lá voçê poderá vizualizar suas aulas do dia o horario e a sala:', link='https://mundo.uniateneu.edu.br/#Notas')
    elif escolha == '4':
        return render_template('index.html', msg="Acesse o link Para Realizar o Download do calendário acadêmico", link="https://docs.google.com/uc?export=download&id=1RoDBSNiWZSBCISMycPHVCtC3Ci69RUFG")
    elif escolha == '5':
        return render_template('index.html', msg="Acesse o Link para a emissão de relatorios", link="https://uniateneu.itvix.com.br/FrameHTML//web/app/edu/PortalEducacional/#/relatorios")
    elif escolha == '6':
        return render_template('index.html', msg="Acesse o link e siga o passo a passo para a realização da rematrícula", link="https://uniateneu.itvix.com.br/FrameHTML//web/app/edu/PortalEducacional/#/es/matricula/apresentacao")
    elif escolha == '7':
        return render_template('index.html', msg="Acesse o link para visualizar sua grade curricular", link="https://uniateneu.itvix.com.br/FrameHTML//web/app/edu/PortalEducacional/#/grade-curricular")
    elif escolha == '8':
        return render_template('index.html', msg="Caso não tenha resolvido suas duvidás ligue para 0800 006 1717 e tire suas dúvidas com um dos nossos atendentes")
    elif escolha == '9':
        return render_template('index.html', msg="Saindo...")
    else:
        return render_template('index.html', msg="Opção inválida. Digite um número válido de 1 a 9.")


if __name__ == "__main__":
    app.run(debug=True)