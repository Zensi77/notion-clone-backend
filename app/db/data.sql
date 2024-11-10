-- Tareas para Alice Johnson
INSERT INTO Tareas (id, title, description, state, prioridad, fecha_inicio, fecha_fin, user_id) VALUES
('d2d3d3e3-f5f5-4a2e-af1b-0d0f0d0f0d0f', 'Submit report', 'Submit the monthly sales report', 'NO_COMENZADO', 'ALTA', '2024-11-10', NULL, 'a8b8c8d8-e8f8-4c8b-af23-0a0f0a0f0a0f'),
('e3f4f5f6-f4f4-4b5c-bd3f-0e0f0e0f0e0f', 'Client meeting', 'Meet with client to discuss project goals', 'EN_PROGRESO', 'MEDIA', '2024-11-08', NULL, 'a8b8c8d8-e8f8-4c8b-af23-0a0f0a0f0a0f'),
('f5f6f7f8-b5b5-4f6d-ac2e-0f0f0f0f0f0f', 'Team lunch', 'Arrange team lunch for Friday', 'TERMINADA', 'BAJA', '2024-11-05', '2024-11-05', 'a8b8c8d8-e8f8-4c8b-af23-0a0f0a0f0a0f'),
('a1b2b3b4-f5f5-4d7e-ae3b-0a0f0a0f0a0f', 'Budget review', 'Review budget allocations for Q4', 'NO_COMENZADO', 'ALTA', '2024-11-11', NULL, 'a8b8c8d8-e8f8-4c8b-af23-0a0f0a0f0a0f'),
('b2c3c4c5-b5b5-4a8e-af7f-0b0f0b0f0b0f', 'Send invoices', 'Send outstanding invoices to clients', 'EN_PROGRESO', 'MEDIA', '2024-11-15', NULL, 'a8b8c8d8-e8f8-4c8b-af23-0a0f0a0f0a0f');

-- Tareas para Bob Smith
INSERT INTO Tareas (id, title, description, state, prioridad, fecha_inicio, fecha_fin, user_id) VALUES
('c3d4d5d6-e6e6-4c9e-bd4f-0c0f0c0f0c0f', 'Code review', 'Review recent code changes', 'NO_COMENZADO', 'MEDIA', '2024-11-06', NULL, 'b9c9d9e9-f9a9-4c9f-be3d-0b0f0b0f0b0f'),
('d4e5f6f7-c7c7-4a0e-ab2d-0d0f0d0f0d0f', 'Project planning', 'Plan new project milestones', 'EN_PROGRESO', 'ALTA', '2024-11-07', NULL, 'b9c9d9e9-f9a9-4c9f-be3d-0b0f0b0f0b0f'),
('e5f6a7b8-d8d8-4f1d-af3e-0e0f0e0f0e0f', 'Documentation', 'Update project documentation', 'TERMINADA', 'BAJA', '2024-11-01', '2024-11-01', 'b9c9d9e9-f9a9-4c9f-be3d-0b0f0b0f0b0f'),
('f6a7b8c9-a9a9-4d2f-bc4d-0f0f0f0f0f0f', 'Feedback session', 'Collect feedback from team', 'NO_COMENZADO', 'MEDIA', '2024-11-09', NULL, 'b9c9d9e9-f9a9-4c9f-be3d-0b0f0b0f0b0f'),
('a8b9c0d1-d1d1-4d3e-ab0f-0a0f0a0f0a0f', 'System upgrade', 'Schedule system maintenance', 'EN_PROGRESO', 'ALTA', '2024-11-13', NULL, 'b9c9d9e9-f9a9-4c9f-be3d-0b0f0b0f0b0f');

-- Tareas para Charlie Brown
INSERT INTO Tareas (id, title, description, state, prioridad, fecha_inicio, fecha_fin, user_id) VALUES
('b1c2d3e4-f1f1-4a2e-af5b-0b0f0b0f0b0f', 'Design UI', 'Create new UI designs for the website', 'NO_COMENZADO', 'ALTA', '2024-11-12', NULL, 'c0d0e0f0-a0b0-4d0e-ab1f-0c0f0c0f0c0f'),
('c2d3e4f5-e2e2-4b5e-bc3d-0c0f0c0f0c0f', 'Bug fixing', 'Fix bugs reported by the users', 'EN_PROGRESO', 'BAJA', '2024-11-14', NULL, 'c0d0e0f0-a0b0-4d0e-ab1f-0c0f0c0f0c0f'),
('d3e4f5a6-a3a3-4f7d-af1e-0d0f0d0f0d0f', 'API integration', 'Integrate new third-party API into the system', 'TERMINADA', 'MEDIA', '2024-11-02', '2024-11-02', 'c0d0e0f0-a0b0-4d0e-ab1f-0c0f0c0f0c0f'),
('e4f5a6b7-b4b4-4d0f-ab4c-0e0f0e0f0e0f', 'User testing', 'Conduct user testing for the new features', 'NO_COMENZADO', 'ALTA', '2024-11-16', NULL, 'c0d0e0f0-a0b0-4d0e-ab1f-0c0f0c0f0c0f'),
('f5a6b7c8-c5c5-4d2e-bd0f-0f0f0f0f0f0f', 'Project retrospective', 'Host a retrospective meeting with the team', 'EN_PROGRESO', 'MEDIA', '2024-11-17', NULL, 'c0d0e0f0-a0b0-4d0e-ab1f-0c0f0c0f0c0f');
