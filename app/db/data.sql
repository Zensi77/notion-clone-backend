-- Usuarios con contraseñas hasheadas
INSERT INTO Usuarios (id, name, email, password) VALUES
('a8b8c8d8-e8f8-11ec-b939-0242ac120002', 'Alice Johnson', 'alice.johnson@example.com', '$2b$12$ql6HgA3Ax23FdWti7lwShOaQCT4PCWYZCRjTxujgYZX82UMHh2uEu'),
('b9c9d9e9-f9g9-11ec-b939-0242ac120002', 'Bob Smith', 'bob.smith@example.com', '$2b$12$4EOO4pBOWt9ZmF72FcUNbOToxISZV6IFDk.Ls9RHTtR5pRHhfsXTa'),
('c0d0e0f0-g0h0-11ec-b939-0242ac120002', 'Charlie Brown', 'charlie.brown@example.com', '$2b$12$V8YrKBHnW4HK2fSyVj/RTOgfOOWHuRUnqL61cI5zTysZmny.PZcXm');

-- Tareas para Alice Johnson
INSERT INTO Tareas (id, title, description, state, prioridad, fecha_inicio, fecha_fin, user_id) VALUES
('d2d3d3e3-f5g5-11ec-b939-0242ac120002', 'Submit report', 'Submit the monthly sales report', 'NO_COMENZADO', 'ALTA', '2024-11-10 09:00:00', NULL, 'a8b8c8d8-e8f8-11ec-b939-0242ac120002'),
('e3f4g5h6-h4i4-11ec-b939-0242ac120002', 'Client meeting', 'Meet with client to discuss project goals', 'EN_PROGRESO', 'MEDIA', '2024-11-08 14:00:00', NULL, 'a8b8c8d8-e8f8-11ec-b939-0242ac120002'),
('f5g6h7j8-j5k5-11ec-b939-0242ac120002', 'Team lunch', 'Arrange team lunch for Friday', 'TERMINADA', 'BAJA', '2024-11-05 12:00:00', '2024-11-05 13:00:00', 'a8b8c8d8-e8f8-11ec-b939-0242ac120002'),
('g7h8i9j0-k5l5-11ec-b939-0242ac120002', 'Budget review', 'Review budget allocations for Q4', 'NO_COMENZADO', 'ALTA', '2024-11-11 10:00:00', NULL, 'a8b8c8d8-e8f8-11ec-b939-0242ac120002'),
('h9i0j1k2-l5m5-11ec-b939-0242ac120002', 'Send invoices', 'Send outstanding invoices to clients', 'EN_PROGRESO', 'MEDIA', '2024-11-15 09:00:00', NULL, 'a8b8c8d8-e8f8-11ec-b939-0242ac120002');

-- Tareas para Bob Smith
INSERT INTO Tareas (id, title, description, state, prioridad, fecha_inicio, fecha_fin, user_id) VALUES
('i2j3k4l5-m6n6-11ec-b939-0242ac120002', 'Code review', 'Review recent code changes', 'NO_COMENZADO', 'MEDIA', '2024-11-06 11:00:00', NULL, 'b9c9d9e9-f9g9-11ec-b939-0242ac120002'),
('j4k5l6m7-n7o7-11ec-b939-0242ac120002', 'Project planning', 'Plan new project milestones', 'EN_PROGRESO', 'ALTA', '2024-11-07 10:00:00', NULL, 'b9c9d9e9-f9g9-11ec-b939-0242ac120002'),
('k6l7m8n9-o8p8-11ec-b939-0242ac120002', 'Documentation', 'Update project documentation', 'TERMINADA', 'BAJA', '2024-11-01 09:00:00', '2024-11-01 10:30:00', 'b9c9d9e9-f9g9-11ec-b939-0242ac120002'),
('l8m9n0o1-p9q9-11ec-b939-0242ac120002', 'Feedback session', 'Collect feedback from team', 'NO_COMENZADO', 'MEDIA', '2024-11-09 15:00:00', NULL, 'b9c9d9e9-f9g9-11ec-b939-0242ac120002'),
('m9o1p2q3-q0r0-11ec-b939-0242ac120002', 'System upgrade', 'Schedule system maintenance', 'EN_PROGRESO', 'ALTA', '2024-11-13 10:00:00', NULL, 'b9c9d9e9-f9g9-11ec-b939-0242ac120002');

-- Tareas para Charlie Brown
INSERT INTO Tareas (id, title, description, state, prioridad, fecha_inicio, fecha_fin, user_id) VALUES
('l3m9n0o1-p9q9-11ec-b939-0242ac120002', 'Design UI', 'Create new UI designs for the website', 'NO_COMENZADO', 'ALTA', '2024-11-12 09:00:00', NULL, 'c0d0e0f0-g0h0-11ec-b939-0242ac120002'),
('m1o1p2q3-q0r0-11ec-b939-0242ac120002', 'Bug fixing', 'Fix bugs reported by the users', 'EN_PROGRESO', 'BAJA', '2024-11-14 14:00:00', NULL, 'c0d0e0f0-g0h0-11ec-b939-0242ac120002'),
('n0p1q2r3-s0t0-11ec-b939-0242ac120002', 'API integration', 'Integrate new third-party API into the system', 'TERMINADA', 'MEDIA', '2024-11-02 08:30:00', '2024-11-02 09:30:00', 'c0d0e0f0-g0h0-11ec-b939-0242ac120002'),
('o1p2q3r4-t1u1-11ec-b939-0242ac120002', 'User testing', 'Conduct user testing for the new features', 'NO_COMENZADO', 'ALTA', '2024-11-16 11:00:00', NULL, 'c0d0e0f0-g0h0-11ec-b939-0242ac120002'),
('p2q3r4s5-u2v2-11ec-b939-0242ac120002', 'Project retrospective', 'Host a retrospective meeting with the team', 'EN_PROGRESO', 'MEDIA', '2024-11-17 10:00:00', NULL, 'c0d0e0f0-g0h0-11ec-b939-0242ac120002');
