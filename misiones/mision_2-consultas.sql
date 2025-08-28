USE ventas;

-- Comerciales que no han vendido nunca
SELECT c.nombre, c.apellido1
FROM comercial c
LEFT JOIN pedido p ON c.id = p.id_comercial
WHERE p.id IS NULL;

-- Promedio del valor de los pedidos de cada año
SELECT YEAR(fecha) AS anio, AVG(total) AS promedio_pedido
FROM pedido
GROUP BY anio
ORDER BY anio;

-- Ventas totales de cada Comercial
SELECT c.nombre, c.apellido1, SUM(p.total) AS total_ventas
FROM comercial c
JOIN pedido p ON c.id = p.id_comercial
GROUP BY c.id
ORDER BY total_ventas DESC;

-- Pedidos mas recientes de cada cliente
SELECT
    cl.nombre AS nombre_cliente,
    cl.apellido1 AS apellido_cliente,
    p.fecha AS fecha_ultimo_pedido,
    p.total AS total_ultimo_pedido
FROM
    cliente cl
JOIN
    pedido p ON cl.id = p.id_cliente
WHERE
    (cl.id, p.fecha) IN (
        SELECT id_cliente, MAX(fecha)
        FROM pedido
        GROUP BY id_cliente
    )
ORDER BY
    p.fecha DESC;