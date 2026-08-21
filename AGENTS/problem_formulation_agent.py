def run(context):
    return {"agent":"problem_formulation","objective":context.get("objective"),"assumptions":context.get("assumptions",[]),"questions":["What is being asked?","What physical regime and constraints apply?"]}
