from io import BytesIO
from flask import Flask, request, jsonify, send_file
from . import tasks

application = Flask("image-randomizer")


@application.route("/randomize", methods=["POST"])
def randomize():
    if not request.mimetype.startswith("image/png"):
        return jsonify({"error": "Ooops! Só sei lidar com imagens PNG!"}), 400

    token = tasks.enqueue_randomize_image_task(request.get_data())
    return jsonify({"token": token})


@application.route("/randomize/<token>/status", methods=["GET"])
def randomize_status(token):
    task = tasks.get_task_result(token)
    if task["status"] in ("errored",):
        return jsonify({"error": str(task["exc"])})

    return jsonify({"status": task["status"]})


@application.route("/randomize/<token>/result", methods=["GET"])
def randomize_result(token):
    task = tasks.get_task_result(token)
    if task["status"] not in ("finished",):
        return jsonify({"message": "not found"}), 404

    return send_file(BytesIO(task["result"]), mimetype="image/png")
