<?php
	if($_POST["message"]) {
		mail("ostroverhovslava@gmail.com", "Here is the subject line",
		$_POST["insert your message here"]. "From: andreykae28@gmail.com");
	}
?>