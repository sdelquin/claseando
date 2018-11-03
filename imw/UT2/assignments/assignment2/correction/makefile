# makefile para corregir la actividad 2
# make <num_actividad> URL="<url al raw del fichero python>"
1:
	curl --silent ${URL} | python - 0 1 2   # -2 
	curl --silent ${URL} | python - 1 1 2   # Sin solución real
	curl --silent ${URL} | python - 1 -5 6  # 3, 2
2:
	curl --silent ${URL} | python - 2 4 7 8 3 5 # (3, 5) con distancia 1.4142135623730951
3:
	curl --silent ${URL} | python - 7	# NOTABLE
	curl --silent ${URL} | python - 2	# SUSPENSO 
	curl --silent ${URL} | python - 9	# SOBRESALIENTE
	curl --silent ${URL} | python - 10	# MATRÍCULA DE HONOR
	curl --silent ${URL} | python - 12	# ERROR
	curl --silent ${URL} | python - -1	# ERROR
4:
	curl --silent ${URL} -o p4.py
	python p4.py 5 # diámetro: 10 | perímetro: 31.41 | área: 78.53
	rm p4.py
