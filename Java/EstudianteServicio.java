package utn.estudiante.servicio;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import utn.estudiante.modelo.Estudiantes2022;
import utn.estudiante.repositorio.EstudianteRepositorio;

import java.util.List;

@Service
public class EstudianteServicio implements IEstudianteServicio{
    @Autowired
    private EstudianteRepositorio estudianteRepositorio;
    @Override //Implementacion de la interface
    public List<Estudiantes2022> listarEstudiantes() {
        List<Estudiantes2022> estudiantes= estudianteRepositorio.findAll();
        return estudiantes;
    }

    @Override
    public Estudiantes2022 buscarEstudiantePorId(Integer idestudiante2022) {

        Estudiantes2022 estudiante= estudianteRepositorio.findById(idestudiante2022).orElse(null);
        return estudiante;
    }

    @Override
    public void guardarEstudiante(Estudiantes2022 estudiante) {
        estudianteRepositorio.save(estudiante);//Guardar estudiante actualizando o agregando
    }

    @Override
    public void eliminarEstudiante(Estudiantes2022 estudiante) {
        estudianteRepositorio.delete(estudiante);
    }
}
