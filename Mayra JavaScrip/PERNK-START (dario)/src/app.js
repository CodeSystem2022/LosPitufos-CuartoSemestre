
import express from "express";
import morgan from "morgan";
import tareasRouters from "./router/tareas.routes.js"
import autRoutes from "./router/auth.routes.js"


const app = express();
app.use(expres.json());
app.use(express.urlencoded({extended: false}));
app.use(morgan("dev"));




app.get("/", ( req,res) => res.json({ message: "bienvenidos "}))
export default app;