import sys 
import io
import shutil
import re

class student:
    def __init__(self,array):
        self.data = []
        array_sep = array.split("\t")
        status_materias_1 = []
        status_materias_2 = []
        status_materias_3 = []
        status_materias_4 = []
        status_optativas = []
        intencion_optativas = []
        #print(array_sep)
        self.fecha = array_sep[0] 
        self.nombre = array_sep[1]
        self.apellido = array_sep[2]
        self.numAlumno = array_sep[3]
        self.email = array_sep[4]
#esto se puede mejorar usando dictionaries
        for i in range(len(materias_1)):
        	status_materias_1.append(array_sep[5+i])
        self.Primero = status_materias_1
        for i in range(len(materias_2)):
        	status_materias_2.append(array_sep[5+len(materias_1)+i])
        self.Segundo = status_materias_2
        for i in range(len(materias_3)):
        	status_materias_3.append(array_sep[5+len(materias_1)+len(materias_2)+i])
        self.Tercero = status_materias_3
        for i in range(len(materias_4)):
        	status_materias_4.append(array_sep[5+len(materias_1)+len(materias_2)+len(materias_3)+i])
        self.Cuarto = status_materias_4
        opt = array_sep[5+len(materias_1)+len(materias_2)+len(materias_3)+len(materias_4)].split(",")
#		for i in range(len(opt)):
#			status_optativas.append(opt[i])
        self.Optativas = opt
        optIntencion = array_sep[5+len(materias_1)+len(materias_2)+len(materias_3)+len(materias_4)+1].split(",")
#		for i in range(len(optIntencion)):
#			intencion_optativas.append(optIntencion[i])
        TodoCursado = status_materias_1+status_materias_2+status_materias_3+status_materias_4+opt
        #TodoCursado = append(status_materias_1)
        #TodoCursado = append(status_materias_2)
        #TodoCursado = append(status_materias_3)
        #TodoCursado = append(status_materias_4)
        #TodoCursado = append(opt)
        
        self.TodoCursado = TodoCursado
        self.Cursar = optIntencion
        
    def check(self):
        
        nuevas = []
        puedeCursar = []
        corrMecanicaII = ["Mecánica Analítica"] #materias_3[0]
        corrMecanicaEstadisticaII = ["Mecánica Estadística I"] #materias_4[2]
        corrMetodosdelaFisicaMatematica = ["Matemáticas Especiales II"] #materias_3[1]
        corrSeminariodeFisicadelSolido = ["Mecánica Estadística I"] #materias_4[2]
        corrSeminariodeParticulasyCampos = ["Mecanica Cuántica II"] #materias_4[0]
        corrSeminariodeMecanicaCuantica = ["Mecanica Cuántica II","Mecánica Estadística I"] #materias_4[0], materias_4[2]
        corrSeminariodeOpticaAvanzada = ["Electromagnetismo","Mecánica Cuántica I"] # materias_3[2]
        corrSeminariodeFisicaNuclear = ["Mecanica Cuántica II","Mecánica Estadística I","Experimentos Cuánticos II"] #materias_4[0], materias_4[2], materias_4[1]
        corrSimulacionesComputacionalesenFisica = ["Mecánica Estadística I"] #materias_4[2]
        corrTermodinamica = ["Física General IV","Física Experimental IV","Matemáticas Especiales I","Física Macroscópica"] #materias_2[3],materias_2[4],materias_2[5],materias_2[6],
        corrTopicosdeMateriaCondensada = ["X"]
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        print("Situacion del alumno "+self.nombre+" "+self.apellido)
        print("Conflictos: ")
        
        listaOptativas = ["Mecánica II","Mecánica Estadística II","Métodos de la Física Matemática","Seminario de Física del Sólido","Seminario de Partículas y Campos","Seminario de Mecánica Cuántica","Seminario de Optica Avanzada","Seminario de Física Nuclear","Simulaciones Computacionales en Física","Termodinámica","Álgebra lineal: Aplicaciones Físicas", "Electromagnetismo 2", "Elementos de la Teoría Cuántica de Campos", "Introducción a la Relatividad General", "Física de la Materia Blanda", "Tópicos de Materia Condensada, ciencia de materiales y nanociencia"]
        listaOptativas_FisMed = ["Procesos estocásticos y su aplicación al modelo de sistemas físicos, químicos y biológicos","Computación","Electrónica", "Análisis de señales", "Biofísica"]
        listaOptativas_Bio = ["Biofisicoquímica","Biología"]
        listaOptativas_Mate = ["Geometría Diferencial", "Elementos de matetmática aplicada", "Topología", "Análisis Numérico I"]
        listaOptativas_Obser = ["Computación","Dinámica no lineal","Análisis Numérico","Introducción a la Astrofísica Relativista"]
        listaOptativas_Posgrado = ["Métodos de geometría diferencial en Teoría de la Información","Probabilidades y estadísitca en Física Experimental"]

materias_1 = ["Física General I", "Física Experimental I", "Análisis Matemático I", "Algebra", "Física General II", "Física Experimental II"] 
materias_2 = ["Física General III", "Física Experimental III", "Análisis Matematico II", "Física General IV", "Física Experimental IV", "Matemáticas Especiales I", "Física Macroscópica"]
materias_3 = ["Mecánica Analítica", "Matemáticas Especiales II", "Electromagnetismo", "Experimentos Electromagnéticos", "Mecánica Cuántica I", "Experimentos Cuánticos I"]
materias_4 = ["Mecanica Cuántica II", "Experimentos Cuánticos II", "Mecánica Estadística I"]

        for i in self.Cursar:
            if not any(i in s for s in listaOptativas):
                nuevas.append(i)



        if any("Métodos de geometría diferencial en Teoría de la Información" in s for s in self.Cursar):
        if any("Probabilidades y estadísitca en Física Experimental" in s for s in self.Cursar):

        if any("Dinámica no lineal" in s for s in self.Cursar):
        if any("Análisis Numérico" in s for s in self.Cursar):
        if any("Introducción a la Astrofísica Relativista" in s for s in self.Cursar):

        if any("Geometría diferencial" in s for s in self.Cursar):
        if any("Elementos de matemática aplicada" in s for s in self.Cursar):
        if any("Topología" in s for s in self.Cursar):
        if any("Análisis Numérico I" in s for s in self.Cursar):

        if any("Biología" in s for s in self.Cursar):

        if any("Biofisicoquímica" in s for s in self.Cursar):

        if any("Biofísica" in s for s in self.Cursar):
            self.Segundo[0]
            self.Segundo[6]
                print("No tiene "++" que se requiere para cursar .")
                print("Ojo! Para cursar  necesita "++" y la esta cursando.")

        if any("Procesos estocásticos y su aplicación al modelo de sistemas físicos, químicos y biológicos" in s for s in self.Cursar):
            if((self.Tercero[1] == "A") or self.Tercero[1] == "TP") and (self.Cuarto[2] == "A" or self.Cuarto[2] == "TP")):
                puedeCursar.append("Procesos estocásticos y su aplicación al modelo de sistemas físicos, químicos y biológicos")
            if(self.Tercero[1] == "NC"):
                print("No tiene "+materias_3[1]+" que se requiere para cursar Procesos estocásticos y su aplicación al modelo de sistemas físicos, químicos y biológicos.")
            if(self.Cuarto[2] == "NC"):
                print("No tiene "+materias_4[2]+" que se requiere para cursar Procesos estocásticos y su aplicación al modelo de sistemas físicos, químicos y biológicos.")
            if(self.Tercero[1] == "EC"):
                print("Ojo! Para cursar Procesos estocásticos y su aplicación al modelo de sistemas físicos, químicos y biológicos necesita "+materias_3[1]+" y la esta cursando.")
            if(self.Cuarto[2] == "EC"):
                print("Ojo! Para cursar Procesos estocásticos y su aplicación al modelo de sistemas físicos, químicos y biológicos necesita "+materias_4[2]+" y la esta cursando.")
        if any("Computación" in s for s in self.Cursar):
            if((self.Primero[2] == "A" or self.Primero[2] == "TP") and (self.Segundo[0] == "A" or self.Segundo[0] == "TP")):
                puedeCursar.append("Computación")
            if(self.Primero[2] == "NC"): 
                print("No tiene "+materias_1[2]+" que se requiere para cursar Computación.")
            if(self.Segundo[0] == "NC"):
                print("No tiene "+materias_2[0]+" que se requiere para cursar Computación.")
            if(self.Primero[2] == "EC"):
                print("Ojo! Para cursar Computación necesita "+materias_1[2]+" y la esta cursando.")
            if(self.Segundo[0] == "EC"):
                print("Ojo! Para cursar Computación necesita "+materias_2[0]+" y la esta cursando.")
        if any("Electrónica" in s for s in self.Cursar):
            if(self.Segundo[0] == "NC"): 
                print("No tiene "+materias_2[0]+" que se requiere para cursar Electrónica.")
            if(self.Tercero[1] == "NC"):
                print("No tiene "+materias_3[1]+" que se requiere para cursar Electrónica.")
            if(self.Segundo[0] == "EC"):
                print("Ojo! Para cursar Electrónica necesita "+materias_2[0]+" y la esta cursando.")
            if(self.Tercero[1] == "EC"):
                print("Ojo! Para cursar Electrónica necesita "+materias_3[1]+" y la esta cursando.")
        if any("Análisis de señales" in s for s in self.Cursar):
            if(self.Segundo[0] == "NC"):
                print("No tiene "+materias_2[0]+" que se requiere para cursar Análisis de señales.")
            if(self.Tercero[1] == "NC"):
                print("No tiene "+materias_3[1]+" que se requiere para cursar Análisis de señales.")
            if(self.Segundo[0] == "EC"):
                print("Ojo! Para cursar Análisis de señales necesita "+materias_2[0]+" y la esta cursando.")
            if(self.Tercero[1] == "EC"):
                print("Ojo! Para cursar Análisis de señales necesita "+materias_3[1]+" y la esta cursando.")
        if any("Álgebra lineal" in s for s in self.Cursar):
            if((self.Primero[3] == "A" or self.Primero[3] == "TP") and (self.Primero[0] == "A" or self.Primero[0] == "TP") and (self.Primero[2] == "A" or self.Primero[2] == "TP")):
                puedeCursar.append("Álgebra lineal")
            if(self.Primero[3] == "NC"):
                print("No tiene "+materias_1[3]+" que se requiere para cursar Álgebra lineal.")
            if(self.Primero[0] == "NC"):
                print("No tiene "+materias_1[0]+" que se requiere para cursar Álgebra lineal.")
            if(self.Primero[2] == "NC"):
                print("No tiene "+materias_1[2]+" que se requiere para cursar Álgebra lineal.")
            if(self.Primero[3] == "EC")
                print("Ojo! Para cursar Álgebra lineal necesita "+materias_1[3]+" y la esta cursando.")
            if(self.Primero[0] == "EC")
                print("Ojo! Para cursar Álgebra lineal necesita "+materias_1[0]+" y la esta cursando.")
            if(self.Primero[2] == "EC")
                print("Ojo! Para cursar Álgebra lineal necesita "+materias_1[2]+" y la esta cursando.")
        if any("Electromagnetismo 2" in s for s in self.Cursar):
            if((self.Tercero[0] == "A" or self.Tercero[0] == "TP") and (self.Tercero[1] == "A" or self.Tercero[1] == "TP") and (self.Tercero[2] == "A" or self.Tercero[2] == "TP") and (self.Tercero[3] == "A" or self.Tercero[3] == "TP"))
                puedeCursar.append("Electromagnetismo 2")
            if(self.Tercero[0] == "NC"): 
                print("No tiene "+materias_3[0]+" que se requiere para cursar Electromagnetismo 2.")
            if(self.Tercero[1] == "NC"):
                print("No tiene "+materias_3[1]+" que se requiere para cursar Electromagnetismo 2.")
            if(self.Tercero[2] == "NC"):
                print("No tiene "+materias_3[2]+" que se requiere para cursar Electromagnetismo 2.")
            if(self.Tercero[3] == "NC"):
                print("No tiene "+materias_3[3]+" que se requiere para cursar Electromagnetismo 2.")
            if(self.Tercero[0] == "EC"): 
                print("Ojo! Para cursar Electromagnetismo 2 necesita "+materias_3[0]+" y la esta cursando.")
            if(self.Tercero[1] == "EC"):
                print("Ojo! Para cursar Electromagnetismo 2 necesita "+materias_3[1]+" y la esta cursando.")
            if(self.Tercero[2] == "EC"):
                print("Ojo! Para cursar Electromagnetismo 2 necesita "+materias_3[2]+" y la esta cursando.")
            if(self.Tercero[3] == "EC"):
                print("Ojo! Para cursar Electromagnetismo 2 necesita "+materias_3[3]+" y la esta cursando.")
        if any("Elementos de la Teoría Cuántica de Campos" in s for s in self.Cursar):
            if((self.Cuarto[0] == "A" or self.Cuarto[0] == "TP") and (listaOptativas[2] == "A" or listaOptativas[2] == "TP")
                puedeCursar.append("Elementos de la Teoría Cuántica de Campos")
            if(self.Cuarto[0] == "NC"):
                print("No tiene "+materias_4[0]+" que se requiere para cursar Elementos de la Teoría Cuántica de Campos.")
            if(listaOptativas[2] == "NC"):
                print("No tiene "+listaOptativas[2]+" que se requiere para cursar Elementos de la Teoría Cuántica de Campos.")
            if(self.Cuarto[0] == "EC"):
                print("Ojo! Para cursar Elementos de la Teoría Cuántica de Campos necesita "+materias_4[0]+" y la esta cursando.")
            if(listaOptativas[2] == "EC"):
                print("Ojo! Para cursar Elementos de la Teoría Cuántica de Campos necesita "+listaOptativas[2]+" y la esta cursando.")
        if any("Introducción a la Relatividad General" in s for s in self.Cursar):
            if((listaOptativas[11] == "A" or listaOptativas[11] == "TP") and (listaOptativas[10] == "A" or listaOptativas[10] == "TP"))
                puedeCursar.append("Introducción a la Relatividad General")
            if(listaOptativas[11] == "NC"):  
                print("No tiene "+listaOptativas[11]+" que se requiere para cursar Introducción a la Relatividad General.")
            if(listaOptativas[10] == "NC"): 
                print("No tiene "+listaOptativas[10]+" que se requiere para cursar Introducción a la Relatividad General.")
            if(listaOptativas[11] == "EC"):
                print("Ojo! Para cursar Introducción a la Relatividad General necesita "+listaOptativas[11]+" y la esta cursando.")
            if(listaOptativas[10] == "EC"):
                print("Ojo! Para cursar Introducción a la Relatividad General necesita "+listaOptativas[10]+" y la esta cursando.")
        if any("Física de la Materia Blanda" in s for s in self.Cursar):
            if((self.Tercero[0] == "A" or self.Tercero[0] == "TP") and (self.Tercero[1] == "A" or self.Tercero[1] == "TP") and (self.Tercero[2] == "A" or self.Tercero[2] == "TP") and (self.Tercero[3] == "A" or self.Tercero[3] == "TP") and (self.Tercero[4] == "A" or self.Tercero[4] == "TP") and (self.Tercero[5] == "A" or self.Tercero[5] == "TP")):
                puedeCursar.append("Física de la Materia Blanda")
            if(self.Tercero[0] == "NC"):
                print("No tiene "+materias_3[0]+" que se requiere para cursar Física de la Materia Blanda.")
            if(self.Tercero[1] == "NC"):
                print("No tiene "+materias_3[1]+" que se requiere para cursar Física de la Materia Blanda.")
            if(self.Tercero[2] == "NC"):
                print("No tiene "+materias_3[2]+" que se requiere para cursar Física de la Materia Blanda.")
            if(self.Tercero[3] == "NC"):
                print("No tiene "+materias_3[3]+" que se requiere para cursar Física de la Materia Blanda.")
            if(self.Tercero[4] == "NC"):
                print("No tiene "+materias_3[4]+" que se requiere para cursar Física de la Materia Blanda.")
            if(self.Tercero[5] == "NC"):
                print("No tiene "+materias_3[5]+" que se requiere para cursar Física de la Materia Blanda.")
            if(self.Tercero[0] == "EC"):
                print("Ojo! Para cursar  necesita "+materias_3[0]+" y la esta cursando.")
            if(self.Tercero[1] == "EC"):
                print("Ojo! Para cursar  necesita "+materias_3[1]+" y la esta cursando.")
            if(self.Tercero[2] == "EC"):
                print("Ojo! Para cursar  necesita "+materias_3[2]+" y la esta cursando.")
            if(self.Tercero[3] == "EC"):
                print("Ojo! Para cursar  necesita "+materias_3[3]+" y la esta cursando.")
            if(self.Tercero[4] == "EC"):
                print("Ojo! Para cursar  necesita "+materias_3[4]+" y la esta cursando.")
            if(self.Tercero[5] == "EC"):
                print("Ojo! Para cursar  necesita "+materias_3[5]+" y la esta cursando.")
        if any("Tópicos de Materia Condensada, ciencia de materiales y nanociencia" in s for s in self.Cursar):
            if((listaOptativas[3] == "A" or listaOptativas[3] == "TP") and (self.Cuarto[0] == "A" or self.Cuarto[0] == "TP") and (self.Tercero[0] == "A" or self.Tercero[0] == "TP"))
            if(listaOptativas[3] == "NC"):
                print("No tiene "+listaOptativas[3]+" que se requiere para cursar Tópicos de Materia Condensada, ciencia de materiales y nanociencia.")
            if(self.Cuarto[0] == "NC"):
                print("No tiene "+materias_4[0]+" que se requiere para cursar Tópicos de Materia Condensada, ciencia de materiales y nanociencia.")
            if(self.Tercero[0] == "NC"):
                print("No tiene "+materias_4[0]+" que se requiere para cursar Tópicos de Materia Condensada, ciencia de materiales y nanociencia.")
            if(listaOptativas[3] == "EC"):
                print("Ojo! Para cursar Tópicos de Materia Condensada, ciencia de materiales y nanociencia necesita "+listaOptativas[3]+" y la esta cursando.")
            if(self.Cuarto[0] == "EC"):
                print("Ojo! Para cursar Tópicos de Materia Condensada, ciencia de materiales y nanociencia necesita "+materias_4[0]+" y la esta cursando.")
            if(self.Tercero[0] == "EC"):
                print("Ojo! Para cursar Tópicos de Materia Condensada, ciencia de materiales y nanociencia necesita "+materias_3[0]+" y la esta cursando.")
        if any("Mecánica II" in s for s in self.Cursar):
            if(self.Tercero[0] == "A" or self.Tercero[0] == "TP"):
                puedeCursar.append("Mecánica II")
            if(self.Tercero[0] == "NC"):
                print("No tiene "+materias_3[0]+" que se requiere para cursar Mecánica II.")
            if(self.Tercero[0] == "EC"):
                print("Ojo! Para cursar Mecánica II necesita "+materias_3[0]+" y la esta cursando.")
                puedeCursar.append("Mecánica II")
        if any("Mecánica Estadísitica II" in s for s in self.Cursar):
            if(self.Cuarto[2] == "A" or self.Cuarto[2] == "TP"):
                puedeCursar.append("Mecánica Estadística II")
            if(self.Cuarto[2] == "NC"):
                print("No tiene "+materias_4[2]+" que se requiere para cursar Mecánica Estadística II.")
            if(self.Cuarto[2] == "EC"):
                print("Ojo! Para cursar Mecánica Estadística II necesita "+materias_4[2]+" y la esta cursando.")
                puedeCursar.append("Mecánica Estadística II")
        if any("Métodos de la Física Matemática" in s for s in self.Cursar):
            if(self.Tercero[1] == "A" or self.Tercero[1] == "TP"):
                puedeCursar.append("Métodos de la Física Matemática")
            if(self.Tercero[1] == "NC"):
                print("No tiene "+materias_3[1]+" que se requiere para cursar Métodos de la Física Matemática.")
            if(self.Tercero[1] == "EC"):
                print("Ojo! Para cursar Métodos de la Física Matemática necesita "+materias_3[1]+" y la esta cursando.")
                puedeCursar.append("Métodos de la Física Matemática")
        if any("Seminario de Física del Sólido" in s for s in self.Cursar):
            if(self.Cuarto[2] == "A" or self.Cuarto[2] == "TP"):
                puedeCursar.append("Seminario de Física del Sólido")
            if(self.Cuarto[2] == "NC"):
                print("No tiene "+materias_4[2]+" que se requiere para cursar Seminario de Física del Sólido.")
            if(self.Cuarto[2] == "EC"):
                print("Ojo! Para cursar Seminario de Física del Sólido necesita "+materias_4[2]+" y la esta cursando.")
                puedeCursar.append("Seminario de Física del Sólido")
        if any("Seminario de Partículas y Campos" in s for s in self.Cursar):
            if(self.Cuarto[0] == "A" or self.Cuarto[0] == "TP"):
                puedeCursar.append("Seminario de Partículas y Campos")
            if(self.Cuarto[0] == "NC"):
                print("No tiene "+materias_4[0]+" que se requiere para cursar Seminario de Partículas y Campos.")
            if(self.Cuarto[0] == "EC"):
                print("Ojo! Para cursar Seminario de Partículas y Campos necesita "+materias_4[0]+" y la esta cursando.")
                puedeCursar.append("Seminario de Partículas y Campos")
        if any("Seminario de Mecánica Cuántica" in s for s in self.Cursar):
            if((self.Cuarto[0] == "A" or self.Cuarto[0] == "EC" or self.Cuarto[0] == "TP") and (self.Cuarto[2] == "A" or self.Cuarto[2] == "EC" or self.Cuarto[2] == "TP")):
                puedeCursar.append("Seminario de Mecánica Cuántica")
            if(self.Cuarto[0] == "NC"):
                print("No tiene "+materias_4[0]+" que se requiere para cursar Seminario de Mecánica Cuántica.")
            if(self.Cuarto[0] == "EC"):
                print("Ojo! Para cursar Seminario de Mecánica Cuántica necesita "+materias_4[0]+" y la esta cursando.")
            if(self.Cuarto[2] == "NC"):
                print("No tiene "+materias_4[2]+" que se requiere para cursar Seminario de Mecánica Cuántica.")
            if(self.Cuarto[2] == "EC"):
                print("Ojo! Para cursar Seminario de Mecánica Cuántica necesita "+materias_4[2]+" y la esta cursando.")
        if any("Seminario de Optica Avanzada" in s for s in self.Cursar):
            if(self.Tercero[2] == "A" or self.Tercero[2] == "TP"):
                puedeCursar.append("Seminario de Optica Avanzada")
            if(self.Tercero[2] == "NC"):
                print("No tiene "+materias_3[2]+" que se requiere para cursar Seminario de Optica Avanzada.")
            if(self.Tercero[2] == "EC"):
                print("Ojo! Para cursar Seminario de Optica Avanzada necesita "+materias_3[2]+" y la esta cursando.")
                puedeCursar.append("Seminario de Optica Avanzada")
        if any("Seminario de Física Nuclear" in s for s in self.Cursar):
            if((self.Cuarto[0] == "A" or self.Cuarto[0] == "EC" or self.Cuarto[0] == "TP") and (self.Cuarto[1] == "A" or self.Cuarto[1] == "EC" or self.Cuarto[1] == "TP") and (self.Cuarto[2] == "A" or self.Cuarto[2] == "EC" or self.Cuarto[2] == "TP")):
                puedeCursar.append("Seminario de Física Nuclear")
            if(self.Cuarto[0] == "NC"):
                print("No tiene "+materias_4[0]+" que se requiere para cursar Simulaciones Computacionales en Física.")
            if(self.Cuarto[1] == "NC"):
                print("No tiene "+materias_4[1]+" que se requiere para cursar Simulaciones Computacionales en Física.")
            if(self.Cuarto[2] == "NC"):
                print("No tiene "+materias_4[2]+" que se requiere para cursar Simulaciones Computacionales en Física.")
            if(self.Cuarto[0] == "EC"):
                print("Ojo! Para cursar Seminario de Física Nuclear necesita "+materias_4[0]+" y la esta cursando.")
            if(self.Cuarto[1] == "EC"):
                print("Ojo! Para cursar Seminario de Física Nuclear necesita "+materias_4[1]+" y la esta cursando.")
            if(self.Cuarto[2] == "EC"):
                print("Ojo! Para cursar Seminario de Física Nuclear necesita "+materias_4[2]+" y la esta cursando.")
        if any("Simulaciones Computacionales en Física" in s for s in self.Cursar):
            if(self.Cuarto[2] == "A" or self.Cuarto[2] == "TP"):
                puedeCursar.append("Simulaciones Computacionales en Física")
            if(self.Cuarto[2] == "NC"):
                print("No tiene "+materias_4[2]+" que se requiere para cursar Simulaciones Computacionales en Física.")
            if(self.Cuarto[2] == "EC"):
                print("Ojo! Para cursar Simulaciones Computacionales en Física necesita "+materias_4[2]+" y la esta cursando.")
                puedeCursar.append("Simulaciones Computacionales en Física")
        if any("Termodinámica" in s for s in self.Cursar):
            if((self.Segundo[3] == "A" or self.Segundo[3] == "EC" or self.Segundo[3] == "TP") and (self.Segundo[4] == "A" or self.Segundo[4] == "EC" or self.Segundo[4] == "TP") and (self.Segundo[5] == "A" or self.Segundo[5] == "EC" or self.Segundo[5] == "TP")):
                puedeCursar.append("Termodinámica")
            if(self.Segundo[3] == "NC"):
                print("No tiene "+materias_2[3]+" que se requiere para cursar Termodinámica.")
            if(self.Segundo[4] == "NC"):
                print("No tiene "+materias_2[4]+" que se requiere para cursar Termodinámica.")
            if(self.Segundo[5] == "NC"):
                print("No tiene "+materias_2[5]+" que se requiere para cursar Termodinámica.")
            if(self.Segundo[6] == "NC"):
                print("No tiene "+materias_2[6]+" que se requiere para cursar Termodinámica.")
            if(self.Segundo[3] == "EC"):
                print("Ojo! Para cursar Termodinámica necesita "+materias_2[3]+" y la esta cursando.")
            if(self.Segundo[4] == "EC"):
                print("Ojo! Para cursar Termodinámica necesita "+materias_2[4]+" y la esta cursando.")
            if(self.Segundo[5] == "EC"):
                print("Ojo! Para cursar Termodinámica necesita "+materias_2[5]+" y la esta cursando.")
            if(self.Segundo[6] == "EC"):
                print("Ojo! Para cursar Termodinámica necesita "+materias_2[6]+" y la esta cursando.")
#		if any("Tópicos de Materia Condensada" in s for s in self.Cursar):
            
        
        print("pidio Cursar: ")
        print(self.Cursar)
        print("puede cursar: ")
        print(puedeCursar)
        print("Quiere cursar tambien la nueva materia:")
        print(nuevas)


materias_1 = ["Física General I", "Física Experimental I", "Análisis Matemático I", "Algebra", "Física General II", "Física Experimental II"] 
materias_2 = ["Física General III", "Física Experimental III", "Análisis Matematico II", "Física General IV", "Física Experimental IV", "Matemáticas Especiales I", "Física Macroscópica"]
materias_3 = ["Mecánica Analítica", "Matemáticas Especiales II", "Electromagnetismo", "Experimentos Electromagnéticos", "Mecánica Cuántica I", "Experimentos Cuánticos I"]
materias_4 = ["Mecanica Cuántica II", "Experimentos Cuánticos II", "Mecánica Estadística I"]


def printFullInfo(allStudents):
	for i in range(len(allStudents)):
		print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
		print("El alumno "+allStudents[i].nombre+" ")
		print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

F = open("Resultados.txt","r",encoding='utf-8') 

alumnos = []

i = 0
info = []
for line in F:
    if i == 0:
	    #print(line.split("\t"))
        for j in line.split(" "):
            info.append(j)
    if i >0:
        alumno = student(line)
        alumnos.append(alumno)
    a = int(i)    
    i += 1
#    if i == 2:
#        break
#materia del primer anio:

materias_optativas= []

#print(info)
#printFullInfo(alumnos)
#print("fecha "+alumnos[0].fecha)
#print("Nombre "+alumnos[0].nombre)
#print("Apellido "+alumnos[0].apellido)
#print("Numero de alumno "+alumnos[0].numAlumno)
#print("email "+alumnos[0].email)
#print(""+alumnos[0].fecha)
for i in range(len(alumnos)):
	alumnos[i].check()
