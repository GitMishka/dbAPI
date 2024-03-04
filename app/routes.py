from flask import request, jsonify
from app import app, db
from app.models import TestTable

# Create a new record
@app.route('/test', methods=['POST'])
def create_record():
    name = request.json['name']
    age = request.json['age']
    new_record = TestTable(name=name, age=age)
    db.session.add(new_record)
    db.session.commit()
    return jsonify({'message': 'Record created successfully'}), 201

# Get a single record by ID
@app.route('/test/<int:id>', methods=['GET'])
def get_record(id):
    record = TestTable.query.get(id)
    if record:
        return jsonify({
            'id': record.id,
            'name': record.name,
            'age': record.age,
            'created_at': record.created_at.isoformat()
        })
    else:
        return jsonify({'message': 'Record not found'}), 404

# Get all records
@app.route('/test', methods=['GET'])
def get_all_records():
    all_records = TestTable.query.all()
    return jsonify([{
        'id': record.id,
        'name': record.name,
        'age': record.age,
        'created_at': record.created_at.isoformat()
    } for record in all_records])

# Update a record by ID
@app.route('/test/<int:id>', methods=['PUT'])
def update_record(id):
    record = TestTable.query.get(id)
    if record:
        data = request.get_json()
        record.name = data.get('name', record.name)
        record.age = data.get('age', record.age)
        db.session.commit()
        return jsonify({'message': 'Record updated successfully'})
    else:
        return jsonify({'message': 'Record not found'}), 404

# Delete a record by ID
@app.route('/test/<int:id>', methods=['DELETE'])
def delete_record(id):
    record = TestTable.query.get(id)
    if record:
        db.session.delete(record)
        db.session.commit()
        return jsonify({'message': 'Record deleted successfully'})
    else:
        return jsonify({'message': 'Record not found'}), 404
