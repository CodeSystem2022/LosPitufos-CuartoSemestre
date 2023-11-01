package UTN.tiendaLibro.vistas;

import UTN.tiendaLibro.servicio.LibroServicio;
import lombok.Builder;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.*;

@Component
public class LibroFrom extends JFrame {
    LibroServicio libroServicio;
    private JPanel panel;
    private JTable tablaLibro;
    private DefaultTableModel tablaModeloLibro;

    @Autowired
    public  LibroFrom(LibroServicio libroServicio){
        this.libroServicio = libroServicio;
        iniciarForma();
        agregarButton.addActionListener(e -> agregarLibro());
    }

    private  void iniciarForma(){
        setContentPane(panel);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setVisible(true);
        setSize(900, 700);
        //Para obtener las dimeciones de la ventana
        Toolkit toolkit= Toolkit.getDefaultToolkit();
        Dimension tamanioPantalla= toolkit.getScreenSize();
        int x = (tamanioPantalla.width-getWidth()/2);
        int y = (tamanioPantalla.height-getHeight()/2);
        setLocation(x,y);
    }

    private void agregarLibro(){
        //Leer lod valores del formulario
        if(libroTexto.getText().equals("")){
            mostrarMensaje("Ingresa el nombre del libro");
            libroTexto.requestFocusInWindow();
            return;
        }
        var nombreLibro= libroTexto.getText();
        var autor= autorTexto.getText();
        var precio= Double.parseDouble(precioTexto.getText());
        var existencias= Integer.parseInt(existenciasTexto.getText());
        //Creamos el objeto libro
        var libro= new Libro();
        libro.setNombreLibro(nombreLibro);
        libro.setAutor(autor);
        libro.setPrecio(precio);
        libro.setExistencias(existencias);
    }

    private  void mostrarMensaje(String mensaje){
        JOptionPane.showMessageDialog(this, mensaje);
    }
    private void creatUIComponents(){
        //TODO: place custom component creation code here
    }
}
