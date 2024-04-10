styleNum = """
    QPushButton { 
        background-color: #35374B; 
        border: none; /*1px solid #aaaaaa;*/ 
        color: #333333; 
        padding: 8px 16px; 
        color: #ffffff;
        font-size: 13px; /* Tamaño de letra 16px */
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    } 
    QPushButton:hover { 
        background-color: #344955; 
        border: none; /*1px solid #aaaaaa;*/
    }

    QPushButton:pressed {
        background-color: #50727B;
        border: none; /*1px solid #aaaaaa;*/
    }
    QPushButton:disabled {
        background-color: #25274B;
        border: none; /*1px solid #aaaaaa;*/
        color: #888888;
    }"""

styleOp = """
    QPushButton { 
        background-color: #304D30; 
        border: none; 
        color: #333333; 
        color: #ffffff;
        font-family: Arial, sans-serif; 
        font-size: 10px
    } 
    QPushButton:hover { 
        background-color: #163020;
        border: none;
    }

    QPushButton:pressed {
        background-color: #B6C4B6;
        border: none;
    }
    QPushButton:disabled {
        background-color: #092635;
        border: none;
        color: #999999;
    }"""

styleCombo = """
QComboBox {
    background-color: #FFFFFF; /* Color de fondo blanco */
    border: 1px solid #CCCCCC; /* Borde gris */
    color: #333333; /* Color del texto */
    padding: 5px; /* Espaciado interno */
    font-size: 14px; /* Tamaño de letra 14px */
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; /* Fuente del sistema */
}

QComboBox::drop-down {
    border: none; /* Sin borde en el botón de despliegue */
    background-color: transparent; /* Fondo transparente */
    subcontrol-origin: padding; /* Origen de los subcontroles */
    subcontrol-position: right; /* Posición del botón de despliegue (derecha) */
}

QComboBox::down-arrow {
    image: url(:/icons/arrow_down.png); /* Icono de flecha hacia abajo */
}

QComboBox:hover {
    background-color: #F0F0F0; /* Color de fondo al pasar el cursor */
}

QComboBox::hover:down-arrow {
    image: url(:/icons/arrow_down_hover.png); /* Icono de flecha hacia abajo al pasar el cursor */
}

QComboBox::hover:!hover:down-arrow {
    image: url(:/icons/arrow_down.png); /* Restaura el icono de flecha hacia abajo */
}

QComboBox::drop-down:hover {
    background-color: #E0E0E0; /* Color de fondo del botón de despliegue al pasar el cursor */
}

"""