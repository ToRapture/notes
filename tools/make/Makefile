oshi = "hanamaru"
kotoba = "$(oshi) daisuki"

define wota
	@echo "seno"
	@echo "arg[0] = [$(0)]"
	@echo "arg[1] = [$(1)]"
	@echo "arg[2] = [$(2)]"
endef

all: whoami
	@echo "stage: $@"
	echo "hello"
	# here is a comment
	@echo "silent echo"
	@# here is a silent comment
	@echo "pwd: $$(pwd)"

whoami:
	echo `whoami`
	echo $$(ls)
	echo "oshi=[$(oshi)]"
	echo "kotoba=[$(kotoba)]"

var-lost:
	export suki="aqours"
	echo "suki=[$$suki]"

var-output:
	export suki="aqours"; echo "suki=[$$suki]"

call-wota:
	$(call wota,hikari,yoshiko,hanamaru)

