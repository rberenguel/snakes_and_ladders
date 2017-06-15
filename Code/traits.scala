trait CanSing {
  def sing(tune: String): String = {
    tune
  }
}

case class Singer(name: String, band: String) extends CanSing

trait PlaysGuitar {
  def rock(tune: String): String
}

case class Rocker(name: String, band: String) extends CanSing with PlaysGuitar {
  override def sing(tune: String): String = {
    s"YEAH ${tune}, baby"
  }

  def rock(tune: String): String = {
    s"🎸 ${tune} 🎸"
  }
}

object TraitsExamples {
  def maxRock(rocker: Rocker, tune: String): String =
    s"${rocker.rock(rocker.sing(tune))}"

  def guitarIt(player: PlaysGuitar, tune: String): String =
    s"${player.rock(tune)}"

  def main(args: Array[String]): Unit = {
    val geneSimmons = Rocker("Gene Simmons", "KISS")
    println(maxRock(geneSimmons, "I was made for loving you"))
    println(guitarIt(geneSimmons, "Strutter"))
    //val justinBieber = Singer("Justin Bieber", "himself")
    //maxRock(justinBieber, "some crap")
    // traits.scala:24: error: type mismatch;
    // found   : Singer
    // required: Rocker
  }
}
